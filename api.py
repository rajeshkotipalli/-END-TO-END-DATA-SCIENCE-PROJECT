# train.py

import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.ensemble import RandomForestClassifier

# Load Titanic dataset
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

# Select relevant columns
df = df[['Pclass', 'Sex', 'Age', 'Fare', 'Survived']].dropna()

# Split into features and target
X = df.drop('Survived', axis=1)
y = df['Survived']

# Preprocessing pipelines
numeric_features = ['Age', 'Fare']
categorical_features = ['Pclass', 'Sex']

numeric_transformer = Pipeline(steps=[
    ('scaler', StandardScaler())
])

categorical_transformer = Pipeline(steps=[
    ('encoder', OneHotEncoder())
])

preprocessor = ColumnTransformer(transformers=[
    ('num', numeric_transformer, numeric_features),
    ('cat', categorical_transformer, categorical_features)
])

# Create full pipeline
model_pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', RandomForestClassifier(n_estimators=100, random_state=42))
])

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model_pipeline.fit(X_train, y_train)

# Save the model
with open("model.pkl", "wb") as f:
    pickle.dump(model_pipeline, f)

print("✅ Model trained and saved as model.pkl")
# api.py

from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import pickle

# Load the saved model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# Define request body structure
class Passenger(BaseModel):
    Pclass: int
    Sex: str
    Age: float
    Fare: float

# Initialize app
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Titanic Survival Predictor API is running!"}

@app.post("/predict")
def predict_survival(data: Passenger):
    df = pd.DataFrame([data.dict()])
    prediction = model.predict(df)[0]
    result = "Survived" if prediction == 1 else "Did not survive"
    return {"prediction": result}

