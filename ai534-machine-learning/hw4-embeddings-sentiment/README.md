# HW4: Word Embeddings for Sentiment Classification

**Course:** AI534 (Machine Learning), Oregon State University, Fall 2025
**Assignment:** [hw4.pdf](https://web.engr.oregonstate.edu/~huanlian/teaching/ML/2025fall/unit4/hw4/hw4.pdf) (15 pts)
**Task:** Redo HW2's sentiment classification (movie reviews, `+`/`-`), replacing HW2's sparse bag-of-words features with dense 300-dim word2vec embeddings, pretrained on about 100 billion words of Google News and pre-filtered to just the vocabulary in `train.csv`. Same Kaggle competition and data as HW2; this assignment is about the effect of dense versus sparse representations, not a new task.

The assignment has three required parts, plus deployment and a debrief:
1. Word embeddings: load `embs_train.kv` with `gensim`, explore nearest-neighbor word similarity and word analogies (for example, `king - man + woman` is close to `queen`)
2. Sentence embeddings (average of word vectors) with k-NN, and reimplementing perceptron and averaged perceptron on these dense features instead of HW2's sparse ones
3. Try one other sklearn algorithm (this submission uses TF-IDF with `LinearSVC`)
4. Deployment: best model wins, submit to Kaggle

No `report.pdf` was provided alongside this submission's code, unlike HW1 through HW3. Part 1, the embedding similarity and analogy exploration, an interactive section worth 5 of the 15 points, isn't represented in the uploaded scripts either. Everything below is reconstructed by directly rerunning the provided code against the real data. There's no report to cross-check against this time, so this README should be treated as the primary record rather than a verification of one.

## Results

| Representation | Method | Best dev error | Best k / setting |
|---|---|---|---|
| Embeddings (avg. word2vec) | k-NN (`knn_embeddings.py`) | 27.4% | k=53, cosine |
| One-hot (HW2-style) | k-NN (`knn_onehot_baseline.py`) | 33.8% | k=19, cosine |
| Embeddings | Perceptron, unaveraged (`perceptron_embeddings.py`) | 31.3% | epoch 6 |
| Embeddings | Averaged perceptron (`perceptron_averaged_embeddings.py`) | 24.2% | epoch 5 |
| Embeddings | Averaged perceptron + pruning (`perceptron_averaged_pruned_embeddings.py`) | 24.2% (see note below) | epoch 5 |
| TF-IDF (1-2 grams) | `LinearSVC` (`svm_tfidf.py`) | 24.7% | C=5 |

Compared to the assignment's own hints: k-NN on embeddings around 28% (got 27.4%), k-NN on one-hot around 40% (got 33.8%, better than hinted, though the relative gap of embeddings clearly beating one-hot matches the expected pattern), basic perceptron around 31% (got 31.3%, an exact match), averaged perceptron around 23-24% (got 24.2%, within range), and pruned averaged perceptron around 23.5% (got 24.2%, missing the target because the pruning step turns out to be a no-op, explained below).

`submission.csv` in this repo is the actual submitted file. Confirmed byte-for-byte reproducible by rerunning `perceptron_averaged_pruned_embeddings.py` against the provided data (495 positive, 505 negative predictions, an exact match to the upload).

The core comparison the assignment is testing, dense embeddings versus sparse one-hot, holds up clearly: k-NN dropped from 33.8% (one-hot) to 27.4% (embeddings) just by switching representations, with no other change. Averaging the perceptron mattered even more here than in HW2 (31.3% to 24.2%, a 7-point drop), since dense 300-dim vectors make raw perceptron weights noisier across epochs than HW2's sparse, mostly orthogonal word features. TF-IDF with SVM (24.7%) landed in the same range as averaged perceptron on embeddings (24.2%), a genuinely close contest between engineering sparse features carefully and using pretrained dense features with a simpler learner. That's a fair summary of where NLP stood before contextual embeddings like BERT took over.

## Repo layout

```
hw4-embeddings-sentiment/
├── data/                                          # HW2 data reused (per assignment) + embeddings
│   ├── train.csv                                  # 8,000 labeled training sentences (same as HW2)
│   ├── dev.csv                                    # 1,000 labeled dev sentences (same as HW2)
│   ├── test.csv                                   # 1,000 unlabeled test sentences (same as HW2)
│   └── embs_train.kv                               # word2vec embeddings (300-dim, 14,414 words),
│                                                    #  pre-filtered to train.csv's vocabulary
├── src/
│   ├── nearest_neighbor_check.py                  # exploratory: closest training sentence by embedding
│   ├── knn_embeddings.py                          # Part 2.1.3: k-NN on sentence embeddings (hint ~28%)
│   ├── knn_onehot_baseline.py                     # Part 2.1.4: k-NN on one-hot vectors (hint ~40%)
│   ├── perceptron_embeddings.py                   # Part 2.2.1: basic perceptron on embeddings (hint ~31%)
│   ├── perceptron_averaged_embeddings.py          # Part 2.2.2: averaged perceptron (hint ~23-24%)
│   ├── perceptron_averaged_pruned_embeddings.py   # Part 2.2.4: word pruning, final model, writes submission
│   └── svm_tfidf.py                               # Part 3: TF-IDF + LinearSVC, alternative algorithm
├── submission.csv                                 # final Kaggle submission (actual graded deliverable)
└── requirements.txt
```

## How to reproduce

```bash
cd src
pip install pandas numpy scikit-learn gensim

python3 nearest_neighbor_check.py                    # quick sanity check, no output file
python3 knn_embeddings.py                             # about 15s
python3 knn_onehot_baseline.py                         # about 4 min (dense one-hot matrix is large)
python3 perceptron_embeddings.py                       # about 8s
python3 perceptron_averaged_embeddings.py               # about 8s
python3 perceptron_averaged_pruned_embeddings.py        # about 8s, writes ../submission.csv (final model)
python3 svm_tfidf.py                                    # about 1 min, writes ../submission.csv
```

`knn_onehot_baseline.py` builds a dense `(8000, vocab_size)` NumPy array rather than a sparse matrix, which is why it's much slower than HW2's sparse-vector k-NN despite doing conceptually the same thing. It's a good illustration of why sparse representations exist.

## Notes and known quirks

- The word pruning in `perceptron_averaged_pruned_embeddings.py` doesn't actually prune anything. `pruneWords(train_file, Occurance=0)` keeps words where `count <= Occurance`, called with `Occurance=0`. Every word that appears at all has count of at least 1, so the returned prune set is always empty. The intent, matching HW2 and HW3's pattern of pruning one-count words, was almost certainly `Occurance=1`. As written, this script is functionally identical to `perceptron_averaged_embeddings.py` (confirmed: both produce byte-identical epoch logs when rerun), which is why the "pruned" dev error (24.2%) doesn't reach the assignment's ~23.5% hint. There was no pruning effect to benefit from. It's still the script that produced the actual graded submission, so it's kept as-is here rather than corrected.
- `nearest_neighbor_check.py` doesn't quite match what the assignment asks for in Part 2.1.1/2.1.2 (find the nearest training-set neighbor for the first and second training sentences). As written, it instead computes the embedding for the second row of `test.csv` and finds its nearest neighbor in `train.csv`, a related but different check. Kept as-is since it's a real, working script, just flagged so it isn't mistaken for a direct answer to those two sub-questions.
- Part 1, the embedding similarity and analogy exploration worth 5 of the 15 points, has no corresponding script in this upload. That section is interactive and exploratory (`wv.most_similar(...)`, analogy queries) and likely lived only in the missing report, not in a `.py` file.
- `embs_train.kv` is about 17.6 MB, sizeable for a git repo. If repo size becomes a concern, this is the first candidate to move to Git LFS or exclude with a download-instructions note instead.
