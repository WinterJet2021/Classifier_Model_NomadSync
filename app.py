from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import pickle
from pydantic import BaseModel
from utils import preprocess_text
import numpy as np

# Load model
with open("interest_classifier_model.pkl", "rb") as f:
    model_data = pickle.load(f)

model = model_data['model']
mlb = model_data['mlb']

app = FastAPI()

# Allow frontend to talk to backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class CommentInput(BaseModel):
    comment: str

@app.post("/classify/")
def classify_comment(data: CommentInput):
    processed = preprocess_text(data.comment)
    prediction = model.predict([processed])[0]
    labels = mlb.classes_[prediction.astype(bool)].tolist()
    return {"interests": labels}
