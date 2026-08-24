# HW2: Perceptron and k-NN for Sentiment Classification

**Course:** AI534 (Machine Learning), Oregon State University, Fall 2025
**Assignment:** [hw2.pdf](https://web.engr.oregonstate.edu/~huanlian/teaching/ML/2025fall/unit2/hw2/hw2.pdf) (15 pts)
**Task:** Classify movie review sentences as positive (`+`) or negative (`-`). 8,000 training, 1,000 dev, and 1,000 semi-blind test sentences, exactly 50/50 balanced, submitted and scored through a class Kaggle competition.

The assignment has five required parts plus a debrief:
0. Why the provided text preprocessing steps (lowercasing, splitting punctuation and contractions, quote normalization) matter for ML
1. Naive perceptron baseline (course-provided `train.py`, about 40 lines, bag-of-words via a sparse vector library `svector.py`), then add the missing bias term
2. Implement averaged perceptron using smart/efficient averaging rather than naive re-summing, since this dataset's sparse vectors are too large for the naive approach used in HW1
3. Prune low-frequency words (one-count, then two-count) from the vocabulary as regularization
4. Try one other sklearn algorithm of your choice (this submission uses k-NN with TF-IDF vectorization)
5. Deployment: pick the overall best model, generate the final Kaggle submission

## Results

Numbers below are reproduced by rerunning the code in this repo against the official data, and they match [`hw2-report.pdf`](hw2-report.pdf) exactly. Best dev error, model size, and best k all matched on the first rerun, with no discrepancies to reconcile this time.

| Part | Approach | Best dev error | Model size (`\|w\|`) | Kaggle public score |
|---|---|---|---|---|
| 1 | Naive perceptron (course baseline, no bias) | 30.1% | 16,743 | not submitted |
| 1 | + bias term added | 28.9% | not applicable | 31.0% (rank 7) |
| 2 | Averaged perceptron (with bias) | 26.3% | 15,806 | 26.8% (rank 6) |
| 3 | + prune 1-count words | 25.9% | 8,425 | 27.4% (rank 7) |
| 3 | + prune 2-count words (tried, not kept) | 26.6% | not applicable | not submitted |
| 4 | k-NN + TF-IDF (cosine distance, k=27) | **23.5%** | not applicable | 25.0% (rank 26) |
| 5 | Final deployment: same k-NN model | 23.5% | not applicable | 25.0% (final rank 40, best public score) |

`test.predicted.csv` in this repo is the actual file submitted for grading. Confirmed byte-for-byte reproducible by rerunning `src/knn_tfidf.py` against the provided data (523 positive, 477 negative predictions, matching exactly).

Every stage improved on the last. Adding the bias term let the decision boundary shift off the origin even on this perfectly balanced dataset (report section 1.5), a good reminder that a 50/50 balanced dataset doesn't mean the bias is safe to skip, since it controls where the hyperplane sits rather than just correcting for skew. Averaging stabilized the perceptron across epochs (26.3% vs. 28.9%, with much less epoch-to-epoch variance, report section 2.1). Pruning one-count words roughly halved the model (15,806 to 8,425 features) with a small accuracy gain, but pruning two-count words as well made things worse, a real regularization/underfitting tradeoff rather than a simple "prune more, do better" pattern. Switching to k-NN with TF-IDF and cosine distance gave the biggest single jump (26.3% to 23.5%), outperforming every perceptron variant tried.

**Model inspection (report sections 2.3 and 2.4):** the top 20 most positive and negative learned features are mostly sensible (`engrossing`, `powerful`, `wonderful` vs. `cliche`, `worst`, `boring`), with some noisier entries (`french`, `dots`, `skin` ranked positive) reflecting bag-of-words' blindness to context. The report also walks through specific dev sentences the model got backwards: reviews using negative-coded words (`lacks`, `hideously`, `nagging`) in an overall positive sentence, and the reverse. This illustrates bag-of-words' core limitation, that word polarity isn't fixed but depends on context a "sum of word vectors" representation simply can't see.

## Repo layout

```
hw2-perceptron-sentiment/
├── data/                          # provided by course, not generated
│   ├── train.csv                  # 8,000 labeled training sentences
│   ├── dev.csv                    # 1,000 labeled dev sentences
│   ├── test.csv                   # 1,000 unlabeled (semi-blind) test sentences
│   └── sample_submission.csv      # course-provided example format
├── src/
│   ├── svector.py                 # course-provided sparse vector library (defaultdict-based)
│   ├── naive_perceptron.py        # course baseline: no bias, naive (non-averaged) perceptron
│   ├── perceptron_averaged.py     # Part 1 (bias) and Part 2 (smart-averaged perceptron)
│   ├── perceptron_pruned.py       # Part 3: one-count word pruning
│   └── knn_tfidf.py               # Part 4/5: TF-IDF + k-NN (cosine, distance-weighted), final model
├── test.predicted.csv             # final blind-test predictions (actual graded submission)
└── hw2-report.pdf
```

## How to reproduce

```bash
cd src
pip install pandas numpy scikit-learn

python3 naive_perceptron.py ../data/train.csv ../data/dev.csv     # Part 1 baseline (no bias)
python3 perceptron_averaged.py ../data/train.csv ../data/dev.csv  # Parts 1+2 (bias + averaging)
python3 perceptron_pruned.py ../data/train.csv ../data/dev.csv    # Part 3 (pruning)
python3 knn_tfidf.py                                              # Part 4/5, writes ../test.predicted.csv
```

`knn_tfidf.py` takes no arguments; it reads `../data/{train,dev,test}.csv` directly. The other three take `trainfile devfile` as positional arguments, matching the course's original `train.py` interface. The blind-test predictions they generate (`../review.predicted.blind.csv`) are a side effect of each script's `predict()` call, separate from the dev-error loop.

## Notes and known quirks

- `perceptron_averaged.py`'s final `predict()` call is pointed at `../data/dev.csv` rather than `../data/test.csv`. This looks like an intentional sanity check against known dev labels rather than a bug, since `perceptron_pruned.py` correctly targets `test.csv` for its blind predictions. Worth being aware of if reusing this script for an actual submission.
- The naive perceptron baseline (`naive_perceptron.py`) is the course-provided `train.py`, included unmodified so the "add the bias" comparison in the report is reproducible against its original starting point.
- `knn_tfidf.py` prunes words appearing only once in `train.csv` by default (`Occurance=1`) before vectorizing. The report notes this was found to help; pruning two-count words as well was tried but not kept, since it made dev error worse.
