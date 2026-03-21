# train.py – creates the model for teenage-pg web app

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import joblib
import warnings
warnings.filterwarnings('ignore')

print("=== Training teenage-pg model START ===")

# 1. Load data
df = pd.read_csv('bungoma.csv')
print("Loaded shape:", df.shape)

# 2. Drop high-cardinality column if exists
if 'Village' in df.columns and df['Village'].nunique() > 100:
    df = df.drop('Village', axis=1)
    print("Dropped Village")

# 3. Encode categorical columns
cat_cols = ['SubCounty', 'Ward', 'ContraceptiveAccess', 'EducationPrograms']
encoders = {}

for col in cat_cols:
    if col in df.columns:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col].astype(str))
        encoders[col] = le
        print(f"Encoded: {col}")

# 4. Features & target
X = df.drop('TeenPregnancyRate', axis=1)
y = df['TeenPregnancyRate']

# 5. Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 6. Train
model = RandomForestRegressor(n_estimators=150, max_depth=10, random_state=42, n_jobs=-1)
model.fit(X_train, y_train)

# 7. Evaluate
pred = model.predict(X_test)
rmse = np.sqrt(mean_squared_error(y_test, pred))
r2 = r2_score(y_test, pred)

print(f"RMSE: {rmse:.3f}")
print(f"R²  : {r2:.3f}")

# 8. Save
joblib.dump(model, 'teenage-pg-rf-model.pkl')
joblib.dump(encoders, 'teenage-pg-encoders.pkl')

print("=== Model & encoders saved successfully ===")
print("Now run: streamlit run app.py")
