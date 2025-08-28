from fastapi import FastAPI, Request
from pydantic import BaseModel
from joblib import load
import pandas as pd 

model = load("phish_detector/model/phishing_model.joblib"

app = FastAPI()

class URLRequest(BaseModel):
    features: list

@app.get("/")
def root():
    return {"message": "phishing detection api is running."}

@app.post("/predict")
def predict_url(data: URLRequest):
    try:
        features_df = pd.DataFrame([data.features])
        prediction = model.predict(features_df)[0]
        return {"prediction": int(prediction)}
    except Exception as e:
        return {"error": str(e)}
    