#!/usr/bin/env python3
#Second iteration of the assignment where I add an averaged model to get better results
from __future__ import division # no need for python3, but just in case used w/ python2

import sys
import time
import pandas as pd
from svector import svector
from collections import Counter
def read_from(textfile):
    data = pd.read_csv(textfile)
    for i in range(len(data)):
        id, words, label = data.iloc[i]
        yield (1 if label=="+" else -1, words.split())

def make_vector(words, pruned_words):
    v = svector()
    for word in words:
        if pruned_words is not None and word not in pruned_words:
            v[word] += 1
    v["<bias>"] +=1
    return v
    
def test(devfile, model, prune_set):
    tot, err = 0, 0
    for i, (label, words) in enumerate(read_from(devfile), 1): # note 1...|D|
        err += label * (model.dot(make_vector(words, prune_set))) <= 0
    return err/i  # i is |D| now
            
def trainAveraged(train_file, dev_file, pruned_words, epochs=5,):
    t = time.time()
    best_err = 1.0
    model = svector() 
    wa = svector()       
    c = 0               
    best_model = None
   

    for it in range(1, epochs + 1):
        updates = 0
        for i, (label, words) in enumerate(read_from(train_file), 1):
            sent = make_vector(words,pruned_words)
            if label * (model.dot(sent)) <= 0:
                updates += 1
                model += label * sent
                wa += c * label * sent
            c += 1   
        avg_model = model - (1.0 / c) * wa
        dev_err = test(dev_file, avg_model,pruned_words)
        print("epoch %d, update %.1f%%, dev %.1f%%" % (it, updates / i * 100, dev_err * 100))

        if dev_err < best_err:
            best_err = dev_err
            best_model = avg_model.copy()

    print("best dev err %.1f%%, |w|=%d, time: %.1f secs" % (best_err * 100, len(model), time.time() - t))
    return best_model


def predict(model,pruned_words, test_file, out_csv = "../review.predicted.blind.csv",label_map=None):
    data = pd.read_csv(test_file)
    preds = []
    for _, row in data.iterrows():
        words = row['sentence'].split()
        score = model.dot(make_vector(words,pruned_words))
        label = label_map(score) if label_map else ("+" if score > 0 else "-")
        preds.append(label)
    data['target'] = preds
    data.to_csv(out_csv, index=False)
    print("Saved blind prediction to ",out_csv)

def removeOneWord(train_file='../data/train.csv'):
    df = pd.read_csv(train_file)
    counter = Counter()
    for _, row in df.iterrows():
        sentence = str(row['sentence'])
        for w in sentence.split():
            counter[w] += 1
    return {w for w, cnt in counter.items() if cnt == 1}
    
if __name__ == "__main__":
    pruned_words = removeOneWord()
    best_model = trainAveraged(sys.argv[1], sys.argv[2], pruned_words, 10 )
    predict(best_model, pruned_words,"../data/test.csv","../review.predicted.blind.csv")

