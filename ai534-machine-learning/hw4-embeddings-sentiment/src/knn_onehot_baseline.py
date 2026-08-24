import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

#load train/dev/test
train = pd.read_csv("../data/train.csv")
dev   = pd.read_csv("../data/dev.csv")
test  = pd.read_csv("../data/test.csv") 

#build vocab sets
vocab = sorted({w for sent in train['sentence'] for w in sent.split()})
word2idx = {w: i for i, w in enumerate(vocab)}
vocab_size = len(vocab)

#make one-hot
def sentence_one_hot(sentence):
    vec = np.zeros(vocab_size)
    for w in sentence.split():
        if w in word2idx:
            vec[word2idx[w]] = 1
    return vec

#convert data
X_train = np.array([sentence_one_hot(s) for s in train['sentence']])
y_train = train['target'].values

X_dev = np.array([sentence_one_hot(s) for s in dev['sentence']])
y_dev = dev['target'].values

X_test = np.array([sentence_one_hot(s) for s in test['sentence']])

#find best k
best_k = None
best_dev_err = 1.0

for k in range(1, 100, 2):
    knn = KNeighborsClassifier(n_neighbors=k, metric='cosine', weights='distance')
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_dev)
    dev_err = 1 - accuracy_score(y_dev, y_pred)
    print(f"k={k:2d}  dev_err {dev_err*100:5.1f}%")
    
    if dev_err < best_dev_err:
        best_k = k
        best_dev_err = dev_err

print(f"\nBest k: {best_k}, Dev Error: {best_dev_err*100:.2f}%")

#train on best k
final_knn = KNeighborsClassifier(n_neighbors=best_k, metric='cosine', weights='distance')
final_knn.fit(X_train, y_train)

#predict test set
y_test_pred = final_knn.predict(X_test)

submission = pd.DataFrame({
    "id": test["id"],  
    "target": y_test_pred
})
submission.to_csv("../submission.csv", index=False)