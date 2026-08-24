import sys
import time
import pandas as pd
import numpy as np
from gensim.models import KeyedVectors

wv = KeyedVectors.load('../data/embs_train.kv')

def read_from(textfile):
    data = pd.read_csv(textfile)
    for i in range(len(data)):
        id_, sentence, label = data.iloc[i]
        yield (1 if label=="+" else -1, sentence)

#word embedding
def make_vector(sentence):
    words = sentence.split()
    vectors = [wv[w] for w in words if w in wv]
    if not vectors:
        return np.zeros(wv.vector_size)
    return np.mean(vectors, axis=0)

#get dev error
def test(model, bias):
    err = 0
    for i, (label, sentence) in enumerate(read_from("../data/dev.csv"), 1):
        x = make_vector(sentence)
        err += label * (np.dot(model, x) + bias) <= 0
    return err / i

def trainPerceptron(epochs=10):
    t0 = time.time()
    n_features = wv.vector_size
    model = np.zeros(n_features)
    b = 0
    wa = np.zeros(n_features)
    ba = 0.0
    c = 1 
    best_err = 1.0
    best_model = None
    best_bias = None

    for epoch in range(1, epochs+1):
        updates = 0
        for label, sentence in read_from("../data/train.csv"):
            x = make_vector(sentence)
            if label * (np.dot(model, x) + b) <= 0:
                model += label * x
                b += label
                wa += c * label * x
                ba += c * label
                updates += 1
            c += 1
        w_avg = model - wa / c
        b_avg = b - ba / c

        dev_err = test(w_avg, b_avg)
        print(f"Epoch {epoch:2d}, updates={updates}, dev error={dev_err*100:.2f}%")
        if dev_err < best_err:
            best_err = dev_err
            best_model = w_avg.copy()
            best_bias = b_avg

    print(f"\nBest dev error: {best_err*100:.2f}%, training time: {time.time()-t0:.1f}s")
    return best_model, best_bias

#predict
def predict(model, bias):
    data = pd.read_csv("../data/test.csv")
    preds = []
    for _, row in data.iterrows():
        x = make_vector(row['sentence'])
        label = "+" if (np.dot(model, x) + bias) > 0 else "-"
        preds.append(label)
    data['target'] = preds
    data.to_csv("../submission.csv", index=False)

best_model, best_bias = trainPerceptron(epochs=10)
predict(best_model, best_bias)

