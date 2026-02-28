import pandas as pd
import pickle
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression

# Load dataset
df = pd.read_csv("city_day.csv")

# Basic Preprocessing
df = df.dropna(subset=['AQI'])
df.fillna(df.mean(numeric_only=True), inplace=True)

features = ['PM2.5', 'PM10', 'NO2', 'SO2', 'CO', 'O3']
X = df[features]
y = df['AQI']

# Train Random Forest
rf = RandomForestRegressor(n_estimators=100, random_state=42)
rf.fit(X, y)
pickle.dump(rf, open("rf_model.pkl", "wb"))

# Train Linear Regression
lr = LinearRegression()
lr.fit(X, y)
pickle.dump(lr, open("linear_model.pkl", "wb"))

print("✅ Both models saved successfully!")