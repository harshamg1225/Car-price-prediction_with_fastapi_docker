import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestRegressor
import joblib
import os
from training.train_utils import Data_FILE_PATH, MODEL_DIR, MODEL_PATH


df = (
    pd.read_csv(Data_FILE_PATH)
    .drop_duplicates()
    .drop(columns=["name", "model", "edition"])
)

x = df.drop(columns=["selling_price"])
y = df.iloc[:, -1]


X_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)


num_cols = X_train.select_dtypes(include="number").columns
cat_cols = X_train.select_dtypes(exclude="number").columns


num_pipe = Pipeline(
    steps=[("Imputer", SimpleImputer(strategy="median")), ("scaler", StandardScaler())]
)

cat_pipe = Pipeline(
    steps=[
        ("imputer", SimpleImputer(strategy="constant", fill_value="missing")),
        ("encoder", OneHotEncoder(handle_unknown="ignore", sparse_output=False)),
    ]
)


preprocessor = ColumnTransformer(
    transformers=[("num", num_pipe, num_cols), ("cat", cat_pipe, cat_cols)]
)


regressor = RandomForestRegressor(n_estimators=20, max_depth=8, random_state=42)

rf_model = Pipeline(steps=[("preprocessor", preprocessor), ("regressor", regressor)])


rf_model.fit(X_train, y_train)


os.makedirs(MODEL_DIR, exist_ok=True)
joblib.dump(rf_model, MODEL_PATH)

print("Folder Exists:", os.path.exists(MODEL_DIR))
print("Model Exists:", os.path.exists(MODEL_PATH))
