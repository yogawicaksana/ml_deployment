from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
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

@app.get("/index", response_class=HTMLResponse)
async def get_index(request: Request):
    with open("index.html", "r") as f:
        html_content = f.read()
    return HTMLResponse(content=html_content)