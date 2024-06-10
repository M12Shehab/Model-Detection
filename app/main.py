# -----------------------------------------------------------------------------
# Copyright (c) 2024 Mohammed A. Shehab
# All rights reserved.
#
# This software is licensed under the terms of the MIT license.
# For details, see the LICENSE file in the root directory of this distribution.
# -----------------------------------------------------------------------------

import os
import sys
# get the current working directory
current_dir = os.path.dirname(os.path.abspath(__file__))
# get the parent directory
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
# add the parent directory to the path
sys.path.append(parent_dir)
# Using fastapi for deployment
from fastapi import FastAPI
from pydantic import BaseModel
from app.model.model import predict_pipeline                # import the trained model
from app.model.model import __version__ as model_version    # import the model version to keep CD/CI


app = FastAPI()

# prepare the JSON payload (request body) for the API
class TextIn(BaseModel):
    text: str

# prepare the JSON response for the API
class PredictionOut(BaseModel):
    language: str

# define the API routes
@app.get("/")
def home():
    return {"health_check": "OK", "model_version": model_version}

# define predict API route
@app.post("/predict", response_model=PredictionOut)
def predict(payload: TextIn):
    language = predict_pipeline(payload.text)
    return {"language": language}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)