from app_api.model import model_implement
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return {"All Good": "☕"}

@app.get("/predict")
def predict_values():
    prediction=model_implement()
    return {"Prediction": prediction}


#print(predict_values())
