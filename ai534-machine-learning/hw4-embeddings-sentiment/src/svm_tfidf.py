import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score

train = pd.read_csv("../data/train.csv")
dev   = pd.read_csv("../data/dev.csv")
test  = pd.read_csv("../data/test.csv")

X_train_text = train["sentence"]
y_train      = train["target"]

X_dev_text   = dev["sentence"]
y_dev        = dev["target"]

X_test_text  = test["sentence"]

#build vectorizer
vectorizer = TfidfVectorizer(
    lowercase=True,
    stop_words=None,       
    sublinear_tf=True,
    ngram_range=(1,2),    
    min_df=1,             
    max_df=0.1         
)


X_train = vectorizer.fit_transform(X_train_text)
X_dev   = vectorizer.transform(X_dev_text)
X_test  = vectorizer.transform(X_test_text)


Cs = [0.01, 0.1, 1.4, 1.5, 1.6, 5, 10]

best_C = None
best_dev_err = 1.0

for C in Cs:
    clf = LinearSVC(C=C)
    clf.fit(X_train, y_train)

    y_pred = clf.predict(X_dev)
    dev_err = 1 - accuracy_score(y_dev, y_pred)

    print(f"C={C}  Dev Error = {dev_err*100:.2f}%")

    if dev_err < best_dev_err:
        best_C = C
        best_dev_err = dev_err

print(f"\nBest C = {best_C}, Dev Error = {best_dev_err*100:.2f}%")

final_clf = LinearSVC(C=best_C)
final_clf.fit(X_train, y_train)

y_test_pred = final_clf.predict(X_test)

submission = pd.DataFrame({
    "id": test["id"],
    "target": y_test_pred
})
submission.to_csv("../submission.csv", index=False)
