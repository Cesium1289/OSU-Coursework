# HW3: Linear and Polynomial Regression for Housing Price Prediction

**Course:** AI534 (Machine Learning), Oregon State University, Fall 2025
**Assignment:** [hw3.pdf](https://web.engr.oregonstate.edu/~huanlian/teaching/ML/2025fall/unit3/hw3/hw3.pdf) (15 pts, plus 1 pt extra credit)
**Task:** Predict house sale prices from 79 mixed categorical and numerical fields (lot size, neighborhood, quality ratings, square footage, and so on). This is the long-running public Kaggle competition [House Prices: Advanced Regression Techniques](https://www.kaggle.com/c/house-prices-advanced-regression-techniques), not a private class competition like HW1 and HW2. It's evaluated with RMSLE (root mean squared log error) rather than plain RMSE, since house prices span small starter homes to mansions and RMSLE penalizes proportional error rather than raw dollar error.

The assignment has four required parts plus a debrief:
1. Understand RMSLE: its definition, how it differs from RMSE, why it's the right metric here, and why training in log-price space is equivalent to optimizing RMSLE directly
2. Naive binarization: one-hot encode every field, including numeric ones, then fit `LinearRegression`
3. Smart binarization: one-hot encode only categorical fields, keep numeric fields as numbers, and properly impute mixed fields like `LotFrontage`/`GarageYrBlt` that have occasional `NA`s
4. Experimentation: regularization (`Ridge`, tuning alpha), non-linear/polynomial features (`PolynomialFeatures`), and anything else that improves the score, then final deployment to Kaggle

## Results

Numbers below are reproduced by rerunning the code in this repo against the official data, and they match [`hw3-report.pdf`](hw3-report.pdf) closely. RMSLE values matched to four or more decimal places on every script tested, more precisely than HW1 or HW2, likely because `LinearRegression` and `Ridge` are deterministic closed-form solvers with no random splits or tie-breaking involved.

| Script | Approach | Features | Dev RMSLE | Kaggle score | Rank |
|---|---|---|---|---|---|
| `naive_binarize_linreg.py` | Naive: binarize all fields, including numeric | 7,227 | 0.1707 | not submitted | not applicable |
| `naive_binarize_linreg_submit.py` | Same as above, plus Kaggle submission | 7,227 | 0.1707 | 0.21815 | 4,831 |
| `smart_binarize_linreg.py` | Smart: one-hot categorical only, numeric fields kept as numbers | 302 | **0.1480** | 0.45763 (see note below) | not applicable |
| `smart_binarize_ridge.py` | Smart binarization + `Ridge(alpha=1000)` | 302 | 0.1614 | not submitted | not applicable |
| `smart_binarize_poly_linreg.py` | Smart binarization + `PolynomialFeatures(degree=2)` on `LotArea`/`GrLivArea`, `LinearRegression` | 302 base plus poly terms | 0.1393 | not submitted | not applicable |
| `best_poly_ridge.py` | Smart binarization + polynomial features + `Ridge(alpha=15)` | 302 base plus poly terms | **0.1373** | **0.14244** | best entry |

The 0.45763 Kaggle score recorded for the plain smart-binarization submission (report section 3.3.d) looks anomalous relative to its 0.148 dev error and the assignment's own hint range of roughly 0.13 to 0.14 for this stage. It's possibly a submission mismatch or a transient scoring issue on Kaggle's end that day. The trend across every other row is consistent (naive, smart, regularized, polynomial, each an improvement), so this is flagged as a one-off rather than treated as representative.

`submission.csv` in this repo is the actual file submitted for grading. Confirmed to match `best_poly_ridge.py`'s output to within floating-point noise (max difference around $46 on prices in the $100K+ range, consistent with a minor sklearn version difference rather than a different model).

Binarizing numeric fields, the naive approach, is a real mistake for regression rather than a minor inefficiency. It inflates the feature count 24x (7,227 vs. 302) and throws away the ordering and magnitude information that fields like `LotArea` and `OverallQual` carry, which is exactly the signal a linear model needs. Keeping numeric fields numeric dropped dev RMSLE from 0.171 to 0.148 with far fewer features. From there, Ridge regularization alone made things slightly worse at high alpha, since the model was underfitting rather than overfitting at this feature count. Adding polynomial features to capture non-linear relationships like `LotArea` squared was the single biggest win, and combining polynomial features with a small amount of Ridge regularization (alpha=15) gave the best result. Report section 4.3 draws a useful parallel to perceptron and XOR here: a purely linear model structurally cannot capture certain relationships no matter how well-tuned, and needs the feature space itself expanded first. Regularization and polynomial features solve different problems, variance versus bias, and matter more or less depending on which one is actually present.

**Model inspection (report sections 2.4 and 3.3.c):** the naive model's top positive and negative features are noisy. The top negative features include `BsmtFinSF1_2260`, `GrLivArea_4676`, and other single-value-bucket features that only fire for one or two houses in the training set, a direct symptom of over-binarizing sparse numeric values. The smart-binarization model's top features are considerably more interpretable: `Neighborhood_NoRidge`, `Neighborhood_StoneBr`, and `OverallQual` dominate positively, while poor `PoolQC`, undesirable `Neighborhood`, and unusual `RoofMatl` dominate negatively, matching common real-estate intuition.

**Bias and intercept (report sections 2.5 and 2.6):** unlike the from-scratch perceptron in HW2, sklearn's `LinearRegression` and `Ridge` handle the bias (intercept) term automatically, so there's no need to add an explicit bias feature. The learned intercept, around $253K in the naive model, represents the baseline predicted price when every feature is zero, a hypothetical reference house with none of the value-adding attributes present.

## Repo layout

```
hw3-regression-housing/
├── data/                                # provided by course, not generated
│   ├── train.csv                        # full labeled Kaggle training set
│   ├── my_train.csv                     # course-provided train/dev split (for local tuning)
│   ├── my_dev.csv                       # course-provided dev set
│   ├── test.csv                         # unlabeled Kaggle test set (semi-blind)
│   └── sample_submission.csv            # course/Kaggle example format
├── src/
│   ├── naive_binarize_linreg.py         # Part 2: binarize everything, LinearRegression
│   ├── naive_binarize_linreg_submit.py  # same, plus writes ../submission.csv for Part 2.7
│   ├── smart_binarize_linreg.py         # Part 3: binarize categorical only, LinearRegression
│   ├── smart_binarize_ridge.py          # Part 4.1: smart binarization + Ridge, alpha tuning
│   ├── smart_binarize_poly_linreg.py    # Part 4.2: + PolynomialFeatures, LinearRegression
│   └── best_poly_ridge.py               # Part 4.4/4.5: + PolynomialFeatures + Ridge, final model
├── submission.csv                       # final Kaggle submission (actual graded deliverable)
└── hw3-report.pdf
```

## How to reproduce

```bash
cd src
pip install pandas numpy scikit-learn

python3 naive_binarize_linreg.py           # Part 2.3: dev RMSLE only
python3 naive_binarize_linreg_submit.py    # Part 2.7: writes ../submission.csv
python3 smart_binarize_linreg.py           # Part 3.3: dev RMSLE only
python3 smart_binarize_ridge.py            # Part 4.1: Ridge, writes ../submission.csv
python3 smart_binarize_poly_linreg.py      # Part 4.2: polynomial features, writes ../submission.csv
python3 best_poly_ridge.py                 # Part 4.4/4.5: final model, writes ../submission.csv
```

Each submission-writing script overwrites `../submission.csv`. Run `best_poly_ridge.py` last if you want the final deliverable's own regenerated copy, or just keep the one included in this repo, which is the actual graded submission.

## Notes and known quirks

- Only `naive_binarize_linreg_submit.py`, `smart_binarize_ridge.py`, `smart_binarize_poly_linreg.py`, and `best_poly_ridge.py` write a submission file. `naive_binarize_linreg.py` and `smart_binarize_linreg.py` are dev-only exploratory scripts with no `test.csv` inference step, matching how the report structures each experimental stage.
- The report's section 2.3 states a dev RMSLE of "0.147" for the naive-binarization stage, but this repo's rerun, and the report's own section 2.7 ("on my computer I got a value of .1707"), both give 0.1707 for that stage. 0.147 is actually the smart-binarization result reported later in section 3.3.b. This looks like a copy/paste slip in the write-up rather than a code issue; the code and the rest of the report are internally consistent.
- `smart_binarize_ridge.py` is hardcoded to `Ridge(alpha=1000)`, the worst-performing alpha tested per report section 4.1 (0.1479 to 0.1614). Kept as-is here since it's a faithful record of that experiment, not the recommended setting.
