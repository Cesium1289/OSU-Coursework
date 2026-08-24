#fourth part of the assignment where I use the k-nn mehtod to predict if a sentence is positive or negative
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from collections import Counter

def pruneWords(train_file='../data/train.csv', Occurance=1):
    df = pd.read_csv(train_file)
    counter = Counter()
    for _, row in df.iterrows():
        sentence = str(row['sentence'])
        for w in sentence.split():
            counter[w] += 1
    return {w for w, cnt in counter.items() if cnt <=Occurance}

def RemovePrunedWords(sentence, pruned_words):
    words = str(sentence).split()
    cleaned_words = []
    for w in words:
        if w not in pruned_words:
            cleaned_words.append(w)
    return " ".join(cleaned_words)

#get train/ dev sets 
train_df = pd.read_csv("../data/train.csv")
dev_df = pd.read_csv("../data/dev.csv")
pruned_words = pruneWords('../data/train.csv',0)
x_train = train_df["sentence"]
y_train = train_df["target"]
x_dev = dev_df["sentence"]
y_dev = dev_df["target"]


#prune words
x_train_pruned = [RemovePrunedWords(s,pruned_words) for s in x_train]
x_dev_pruned = [RemovePrunedWords(s,pruned_words) for s in x_dev]

#vectorize the data
vectorizer = TfidfVectorizer(lowercase=False, token_pattern=r"(?u)\b\w+\b")

#transform the train/ dev sets
X_train_vec = vectorizer.fit_transform(x_train_pruned)
X_dev_vec   = vectorizer.transform(x_dev_pruned)

best_k = None
best_dev_err = 1.0

#track k values and their dev error for graph
k_values = []
dev_errors = []

#loop through all k values and find the best
for k in range(1, 100,2):
    knn = KNeighborsClassifier(n_neighbors=k, metric='cosine', weights='distance')
    knn.fit(X_train_vec, y_train)
    y_pred = knn.predict(X_dev_vec)
    dev_err = 1- accuracy_score(y_dev, y_pred)
    print(f"k={k:2d}  dev_err {dev_err*100:5.1f}%")
    if dev_err < best_dev_err:
        best_k = k
        best_dev_err = dev_err
    k_values.append(k)
    dev_errors.append(dev_err)
print(f"\nBest k: {best_k}, Dev Error: {best_dev_err*100:.2f}%")

#refit best k value 
best_knn = KNeighborsClassifier(n_neighbors=best_k)
best_knn.fit(X_train_vec, y_train) 

#pedict on dev set
y_dev_pred_best = best_knn.predict(X_dev_vec)

#build data with predictions
submission_df = pd.DataFrame({
    "id": range(9000, 9000 + len(x_dev)),
    "sentence": x_dev,
    "target": y_dev_pred_best
})

#save to CSV
submission_df.to_csv("../test.predicted.csv", index=False)
print("Saved predictions to blind.test.predicted.csv")

#blind test
df_blind = pd.read_csv("../data/test.csv")
x_blind_pruned = [RemovePrunedWords(s, pruned_words) for s in df_blind["sentence"]]
X_blind_vec = vectorizer.transform(x_blind_pruned)
y_blind_pred = best_knn.predict(X_blind_vec)

df_blind["target"] = y_blind_pred
df_blind.to_csv("../test.predicted.csv", index=False)
print("Saved predictions to test.predicted.csv")

