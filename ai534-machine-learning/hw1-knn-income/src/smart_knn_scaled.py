#third part of the assignment where it is the smart/ scaling
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, MinMaxScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.compose import ColumnTransformer

df = pd.read_csv("../data/income.train.5k.csv")
X = df.drop(columns=["id", "target"]).copy()
y = df["target"].copy()

#process and one-hot encode
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

best_k = None
best_dev_err = 1.0

#track k values and their dev error for graph
k_values = []
dev_errors = []

#loop through all k values and find the best
for k in range(1, 100,2):
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train_proc, y_train)
    y_pred = knn.predict(X_dev_proc)
    dev_err = 1- accuracy_score(y_dev, y_pred)
    print(f"k={k:2d}  dev_err {dev_err*100:5.1f}%")
    if dev_err < best_dev_err:
        best_k = k
        best_dev_err = dev_err
    k_values.append(k)
    dev_errors.append(dev_err)
print(f"\nBest k: {best_k}, Dev Error: {best_dev_err*100:.2f}%")


#save data to file to create graph 
filename = "../results/k_values.csv"
try:
    df = pd.read_csv(filename)
except FileNotFoundError:
    df = pd.DataFrame({"k": k_values})
if "k" not in df.columns or len(df["k"]) != len(k_values):
    df = pd.DataFrame({"k": k_values})
df["smart_scaled"] = dev_errors
df.to_csv(filename, index=False)
print(f"Saved results for smart_scaled to {filename}")

#refit best k value 
best_knn = KNeighborsClassifier(n_neighbors=best_k)
best_knn.fit(X_train_proc, y_train) 

#pedict on dev set
y_dev_pred_best = best_knn.predict(X_dev_proc)

#build data with predictions
submission_df = X_dev.copy()  # start with dev features
submission_df["target"] = y_dev_pred_best  # add predictions
submission_df["id"] = range(6000, 6000 + len(submission_df))  # optional

#order columns
final_columns = [
    "id", "age", "sector", "edu", "marriage", "occupation",
    "race", "sex", "hours", "country", "target"
]
existing_cols = [c for c in final_columns if c in submission_df.columns]
submission_df = submission_df[existing_cols]

#save to CSV
submission_df.to_csv("../income.test.predicted.csv", index=False)
print("Saved predictions to income.test.predicted.csv")

#blind test
df_blind = pd.read_csv("../data/income.test.blind.csv")
X_blind = df_blind.drop(columns=["id"], errors='ignore')
X_blind_proc = preprocessor.transform(X_blind)
y_blind_pred = best_knn.predict(X_blind_proc)

df_blind["target"] = y_blind_pred
df_blind["id"] = range(6000, 6000 + len(df_blind))
df_blind.to_csv("../income.semi_blind.predicted.csv", index=False)
print("Saved predictions to income.test.predicted.csv")