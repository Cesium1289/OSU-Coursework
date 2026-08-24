from gensim.models import KeyedVectors
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

wv = KeyedVectors.load('../data/embs_train.kv')
test = pd.read_csv("../data/test.csv")
train = pd.read_csv("../data/train.csv")
def sentence_embedding(sentence, wv):
    words = sentence.split()                      
    vectors = []
    
    for w in words:
        if w in wv:                               
            vectors.append(wv[w])
    if not vectors:
        return np.zeros(wv.vector_size)           
    return np.mean(vectors, axis=0)               

train_embs =np.array([sentence_embedding(s, wv) for s in train['sentence']])

#embedding for the first sentence
test_emb = sentence_embedding(test['sentence'][1], wv)

sims = cosine_similarity([test_emb], train_embs)[0]

#find the closest
closest_idx = sims.argmax()
closest_sentence = train['sentence'][closest_idx]
closest_label = train['target'][closest_idx]

print("Closest training sentence:", closest_sentence)
print("Label:", closest_label)
print(closest_idx)