import os
import sys
# get the current working directory
current_dir = os.path.dirname(os.path.abspath(__file__))
# get the parent directory
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
# add the parent directory to the path
sys.path.append(parent_dir)

from fastapi import FastAPI
from pydantic import BaseModel
from app.model.model import predict_pipeline
from app.model.model import __version__ as model_version


app = FastAPI()


class TextIn(BaseModel):
    text: str


class PredictionOut(BaseModel):
    language: str


@app.get("/")
def home():
    return {"health_check": "OK", "model_version": model_version}


@app.post("/predict", response_model=PredictionOut)
def predict(payload: TextIn):
    language = predict_pipeline(payload.text)
    return {"language": language}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)