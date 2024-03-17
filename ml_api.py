from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import os 
import pandas as pd

model_path = 'model'

app = FastAPI()

class PredictCaloriesItem(BaseModel):
    TotalDistance: float 
    TotalActiveMinutes: float

with open(os.path.join(model_path, 'model.pkl'), 'rb') as f:
    model = pickle.load(f)

@app.post('/')
async def predict_calories(item:PredictCaloriesItem):
    df = pd.DataFrame([item.model_dump().values()], columns=item.model_dump().keys())
    preds = model.predict(df)
    return {'prediction':int(preds)}