#Fourth part of using our own k-nn
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, MinMaxScaler
from sklearn.metrics import accuracy_score
from sklearn.compose import ColumnTransformer

class MyKNN:
    def __init__(self, k=3, metric='euclidean'):
        assert metric in ('euclidean', 'manhattan')
        self.k = k
        self.metric = metric
        self.X = None
        self.y = None
        self._X_sq = None

    def fit(self, X, y):
        self.X = np.asarray(X)
        self.y = np.asarray(y)
        if self.metric == 'euclidean':
            self._X_sq = np.sum(self.X * self.X, axis=1)
    def _compute_distances(self, queries):
        #vectorized for all queries
        queries = np.asarray(queries)
        if queries.ndim == 1:
            queries = self._compute_distances_manhattan(self, queries,600)

        if self.metric == 'euclidean':
            #||a-b||^2 = ||a||^2 + ||b||^2 - 2 a.b
            X_sq = self._X_sq
            Q_sq = np.sum(queries*queries, axis=1)  #(m,)
            cross = queries.dot(self.X.T)           #(m, n)
            D2 = Q_sq[:, None] + X_sq[None, :] - 2*cross
            D2 = np.maximum(D2, 0.0)
            D = np.sqrt(D2)
        else:
            #manhattan distance
            D = np.sum(np.abs(queries[:, None, :] - self.X[None, :, :]), axis=2)
        return D  #shape (m, n)

    def predict(self, Xq):
        D = self._compute_distances(Xq)  #(m, n)
        k = min(self.k, D.shape[1])

        #get top-k indices for each query
        idx_topk = np.argpartition(D, kth=k-1, axis=1)[:, :k]
        #sort top-k distances
        k_dists = np.take_along_axis(D, idx_topk, axis=1)
        order = np.argsort(k_dists, axis=1)
        idx_sorted = np.take_along_axis(idx_topk, order, axis=1)

        #majority vote
        preds = []
        for neighbors in idx_sorted:
            labels = self.y[neighbors]
            vals, counts = np.unique(labels, return_counts=True)
            max_count = counts.max()
            candidates = vals[counts == max_count]
            preds.append(np.min(candidates)) 
        return np.array(preds)

#load data
df = pd.read_csv("../data/income.train.5k.csv")
X = df.drop(columns=["id", "target"]).copy()
y = df["target"].copy()

#process and one-hot endcode
num_processor = MinMaxScaler(feature_range=(0, 2))
cat_processor = OneHotEncoder(sparse_output=False, handle_unknown='ignore')
preprocessor = ColumnTransformer([
('num', num_processor, ['age','hours']),
('cat', cat_processor, ['sector','edu','marriage','occupation','race','sex','country'])
])

#train/dev split
X_train, X_dev, y_train, y_dev = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=0
)
#transform the train and dev sets
X_train_proc = preprocessor.fit_transform(X_train)
X_dev_proc = preprocessor.transform(X_dev)
print(preprocessor.get_feature_names_out())

best_k = None
best_dev_err = 1.0

#loop through all k values and find the best
for k in range(1, 100,2):
    knn = MyKNN(k=k, metric='euclidean')
    knn.fit(X_train_proc, y_train)
    y_pred = knn.predict(X_dev_proc)
    dev_err = 1 - accuracy_score(y_dev, y_pred)
    print(f"k={k:2d}  dev_err {dev_err*100:5.1f}%")
    if dev_err < best_dev_err:
        best_k, best_dev_err = k, dev_err
print(f"\nBest k: {best_k}, Dev Error: {best_dev_err*100:.2f}%")

#refit best k value
best_knn = MyKNN(k=best_k, metric='euclidean')
best_knn.fit(X_train_proc, y_train) 

#predict on dev set
y_dev_pred_best = best_knn.predict(X_dev_proc)

#build data with predictions
submission_df = X_dev.copy()  
submission_df["target"] = y_dev_pred_best 
submission_df["id"] = range(6000, 6000 + len(submission_df)) 

#order columns
final_columns = [
    "id", "age", "sector", "edu", "marriage", "occupation",
    "race", "sex", "hours", "country", "target"
]
existing_cols = [c for c in final_columns if c in submission_df.columns]
submission_df = submission_df[existing_cols]

#save data to csv
submission_df.to_csv("../income.test.predicted.csv", index=False)
#print("Saved predictions to income.test.predicted.csv")


#blind test
df_blind = pd.read_csv("../data/income.test.blind.csv")
X_blind = df_blind.drop(columns=["id"], errors='ignore')
X_blind_proc = preprocessor.transform(X_blind)
y_blind_pred = best_knn.predict(X_blind_proc)

df_blind["target"] = y_blind_pred
df_blind["id"] = range(6000, 6000 + len(df_blind))
df_blind.to_csv("../income.test.predicted.csv", index=False)
print("Saved predictions to income.test.predicted.csv")
