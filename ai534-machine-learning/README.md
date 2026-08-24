# AI 534: Machine Learning

Machine learning coursework for AI 534 (Oregon State University). Each subfolder is a self-contained homework assignment with its own README, code, and results.

## Projects

| Project | Topic | Best result |
|---|---|---|
| [hw1-knn-income](hw1-knn-income/) | k-nearest neighbors for income classification (`>50K` vs `<=50K`) from census data, including a from-scratch k-NN implementation | 18.4% dev error, 0.172 Kaggle test score |
| [hw2-perceptron-sentiment](hw2-perceptron-sentiment/) | Averaged perceptron and k-NN for movie review sentiment classification (`+`/`-`) using sparse bag-of-words features | 23.5% dev error, 0.250 Kaggle test score |
| [hw3-regression-housing](hw3-regression-housing/) | Linear, polynomial, and Ridge regression for house sale price prediction (public Kaggle "House Prices: Advanced Regression Techniques" competition) | 0.1373 dev RMSLE, 0.14244 Kaggle test score |
| [hw4-embeddings-sentiment](hw4-embeddings-sentiment/) | Redo of HW2's sentiment classification using dense word2vec embeddings instead of sparse one-hot features, with k-NN, averaged perceptron, and SVM | 24.2% dev error (averaged perceptron on embeddings) |

## Structure convention

Each project folder generally follows:

```
project-name/
├── README.md       # problem statement, approach, results
├── data/            # input data (where license/size permits)
├── src/             # all code
├── results/         # generated plots, metrics, tables
└── requirements.txt
```
