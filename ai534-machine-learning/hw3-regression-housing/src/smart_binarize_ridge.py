import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_squared_log_error
from sklearn.linear_model import Ridge

#load data
train = pd.read_csv("../data/my_train.csv")
dev = pd.read_csv("../data/my_dev.csv")

#drop unneeded columns
X_train = train.drop(columns=["Id", "SalePrice"])
y_train = train["SalePrice"]
X_dev = dev.drop(columns=["Id", "SalePrice"])
y_dev = dev["SalePrice"]

#seperate numeric and category columns
numeric_cols = X_train.select_dtypes(include=['int64', 'float64']).columns.tolist()
categorical_cols = X_train.select_dtypes(include=['object']).columns.tolist()

#fill the missing values so it doesn't break
numeric_transformer = SimpleImputer(strategy='median')

#set categorical pipeline
categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='constant', fill_value='Missing')),
    ('onehot', OneHotEncoder(handle_unknown='ignore', sparse_output=True))
])

#combine both pipelines
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numeric_cols),
        ('cat', categorical_transformer, categorical_cols)
    ]
)

#create the model pipeline
model = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', Ridge(alpha=1000))
])

#fit the model
model.fit(X_train, y_train)

#find number of features
num_numeric = len(numeric_cols)
num_categorical = preprocessor.named_transformers_['cat'] \
    .named_steps['onehot'].get_feature_names_out(categorical_cols).shape[0]
total_features = num_numeric + num_categorical
print("Total features:", total_features)

#make prediction
y_pred = model.predict(X_dev)
y_pred = np.maximum(y_pred, 0)
rmsle = np.sqrt(mean_squared_log_error(y_dev, y_pred))
print("RMSLE :", rmsle)

#load test data
test = pd.read_csv("../data/test.csv")
X_test = test.drop(columns=["Id"])

y_test_pred = model.predict(X_test)
y_test_pred = np.maximum(y_test_pred, 0)

#save to CSV
submission = pd.DataFrame({
    "Id": test["Id"],
    "SalePrice": y_test_pred
})

submission.to_csv("../submission.csv", index=False)
print("Submission file created: submission.csv")

#prep to get top features
numeric_features = numeric_cols
categorical_features = preprocessor.named_transformers_['cat'] \
    .named_steps['onehot'].get_feature_names_out(categorical_cols)
all_features = np.concatenate([numeric_features, categorical_features])
coefs = model.named_steps['regressor'].coef_
coef_df = pd.DataFrame({'feature': all_features, 'coef': coefs}).sort_values(by='coef', ascending=False)

print("\nTop 10 positive features:")
print(coef_df.head(10))
print("\nTop 10 negative features:")
print(coef_df.tail(10))
