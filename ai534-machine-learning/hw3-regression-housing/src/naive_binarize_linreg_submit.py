import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_squared_log_error

#load data
train = pd.read_csv("../data/my_train.csv")
dev = pd.read_csv("../data/my_dev.csv")

#drop unneeded columns
X_train = train.drop(columns=["Id", "SalePrice"])
y_train = train["SalePrice"]
X_dev = dev.drop(columns=["Id", "SalePrice"])
y_dev = dev["SalePrice"]

#convert everything to a str
X_train = X_train.astype('str')
X_dev = X_dev.astype('str')

#encode the data
encoder = OneHotEncoder(handle_unknown='ignore', sparse_output=True)
X_train_enc = encoder.fit_transform(X_train)
X_dev_enc = encoder.transform(X_dev)

#fit the model
model = LinearRegression()
model.fit(X_train_enc, y_train)

#make prediction
y_pred = model.predict(X_dev_enc)
y_pred = np.maximum(y_pred, 0)
rmsle = np.sqrt(mean_squared_log_error(y_dev, y_pred))

#load test data
test = pd.read_csv("../data/test.csv")

X_test = test.drop(columns=["Id"])
X_test = X_test.astype(str)

X_test_enc = encoder.transform(X_test)
y_test_pred = model.predict(X_test_enc)

#save to CSV
submission = pd.DataFrame({
    "Id": test["Id"],
    "SalePrice": y_test_pred
})

submission.to_csv("../submission.csv", index=False)
print("Submission file created: submission.csv")
feature_names = encoder.get_feature_names_out(X_train.columns)
coef_df = pd.DataFrame({
    'feature': feature_names,
    'coef': model.coef_
}).sort_values(by='coef', ascending=False)

print("\nTop 10 positive features:")
print(coef_df.head(10))
print("\nTop 10 negative features:")
print(coef_df.tail(10))