#First part of the assignment using the naive approach
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

#load in data
df = pd.read_csv("../data/income.train.5k.csv")
X = df.drop(columns=["id", "target"]).copy()
y = df["target"].copy()


#train/dev split
X_train, X_dev, y_train, y_dev = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=0
)

#process one-hot encode
ohe = OneHotEncoder(handle_unknown="ignore", sparse_output=False)
X_train_enc = ohe.fit_transform(X_train)
X_dev_enc   = ohe.transform(X_dev)


best_k = None
best_dev_err = 1.0
train_err = 1.0

#track k values and their dev error for graph
k_values = []
dev_errors = []

#loop through all k values and find the best
for k in range(1, 100, 2):
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train_enc, y_train)
    y_dev_pred = knn.predict(X_dev_enc)
    y_train_pred = knn.predict(X_train_enc)
    dev_err = 1 - accuracy_score(y_dev, y_dev_pred)
    train_err = 1 - accuracy_score(y_train,y_train_pred)
    print(f"k={k:2d}  train_err {train_err*100:5.1f}%   dev_err {dev_err*100:5.1f}%")
    if dev_err < best_dev_err:
        best_k = k
        best_dev_err = dev_err
    k_values.append(k)
    dev_errors.append(dev_err)
print(f"Best dev error: {best_dev_err*100:.2f}% at k={best_k}")

#save data to file to create graph 
filename = "../results/k_values.csv"
try:
    df = pd.read_csv(filename)
except FileNotFoundError:
    df = pd.DataFrame({"k": k_values})

if "k" not in df.columns or len(df["k"]) != len(k_values):
    df = pd.DataFrame({"k": k_values})
df["naive"] = dev_errors
df.to_csv(filename, index=False)
print(f"Saved results for naive to {filename}")


#refit best k value
best_knn = KNeighborsClassifier(n_neighbors=best_k)
best_knn.fit(X_train_enc, y_train)

#predict on dev set
y_dev_pred_best = best_knn.predict(X_dev_enc)

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

#save data to CSV
submission_df.to_csv("../income.test.predicted.csv", index=False)
print("Saved predictions to income.test.predicted.csv")