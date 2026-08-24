import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from gensim.models import KeyedVectors

wv = KeyedVectors.load('../data/embs_train.kv')

#load train/dev/test
train = pd.read_csv("../data/train.csv")
dev  = pd.read_csv("../data/dev.csv")
test = pd.read_csv("../data/test.csv")

#sentence embedding function
def sentence_embedding(sentence, wv):
    words = sentence.split() 
    vectors = [wv[w] for w in words if w in wv]
    if not vectors:
        return np.zeros(wv.vector_size)
    return np.mean(vectors, axis=0)

#convert data
X_train = np.array([sentence_embedding(s, wv) for s in train['sentence']])
y_train = train['target'].values

X_dev = np.array([sentence_embedding(s, wv) for s in dev['sentence']])
y_dev = dev['target'].values

X_test = np.array([sentence_embedding(s, wv) for s in test['sentence']])

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