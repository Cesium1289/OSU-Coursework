import sys
import time
import pandas as pd
import numpy as np
from gensim.models import KeyedVectors
from collections import Counter

wv = KeyedVectors.load('../data/embs_train.kv')

def pruneWords(train_file='../data/train.csv', Occurance=0):
    df = pd.read_csv(train_file)
    counter = Counter()
    for _, row in df.iterrows():
        for w in str(row['sentence']).split():
            counter[w] += 1
    return {w for w, cnt in counter.items() if cnt <= Occurance}

def RemovePrunedWords(sentence, pruned_words):
    return " ".join([w for w in str(sentence).split() if w not in pruned_words])

def read_from(textfile, pruned_words):
    data = pd.read_csv(textfile)
    for i in range(len(data)):
        _, sentence, label = data.iloc[i]
        sentence = RemovePrunedWords(sentence, pruned_words)
        yield (1 if label=="+" else -1, sentence)

def make_vector(sentence):
    words = sentence.split()
    vectors = [wv[w] for w in words if w in wv]
    if not vectors:
        return np.zeros(wv.vector_size)
    return np.mean(vectors, axis=0)

def test(pruned_words, model, bias):
    tot, err = 0, 0
    for i, (label, sentence) in enumerate(read_from("../data/dev.csv", pruned_words), 1):
        x = make_vector(sentence)
        err += label * (np.dot(model, x) + bias) <= 0
    return err / i

def trainAveraged(epochs=10):
    pruned_words = pruneWords("../data/train.csv", 0)
    t0 = time.time()
    best_err = 1.0
    n_features = wv.vector_size
    model = np.zeros(n_features)
    wa = np.zeros(n_features)
    b = 0
    ba = 0
    c = 1
    best_model = None
    best_bias = None

    for epoch in range(1, epochs+1):
        updates = 0
        for label, sentence in read_from("../data/train.csv", pruned_words):
            x = make_vector(sentence)
            if label * (np.dot(model, x) + b) <= 0:
                model += label * x
                b += label
                wa += c * label * x
                ba += c * label
                updates += 1
            c += 1

        avg_model = model - wa / c
        avg_bias = b - ba / c

        dev_err = test(pruned_words, avg_model, avg_bias)
        print(f"epoch {epoch:2d}, updates {updates}, dev error {dev_err*100:.2f}%")

        if dev_err < best_err:
            best_err = dev_err
            best_model = avg_model.copy()
            best_bias = avg_bias

    print(f"best dev error: {best_err*100:.2f}%, time: {time.time()-t0:.1f}s")
    return best_model, best_bias, pruned_words

#predict
def predict(model, bias, pruned_words):
    data = pd.read_csv("../data/test.csv")
    preds = []
    for _, row in data.iterrows():
        s = RemovePrunedWords(row["sentence"], pruned_words)
        x = make_vector(s)
        label = "+" if (np.dot(model, x) + bias) > 0 else "-"
        preds.append(label)
    data['target'] = preds
    data.to_csv("../submission.csv", index=False)

best_model, best_bias, pruned_words = trainAveraged(epochs=10)
predict(best_model, best_bias, pruned_words)
