from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from model import predict_sentiment

app = FastAPI()

# Allow requests from the frontend (different domain/port)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],    # tighten this in production
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define the shape of the request body
class TextInput(BaseModel):
    text: str

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict")
def predict(input: TextInput):
    result = predict_sentiment(input.text)
    return {
        "sentiment": result["sentiment"],
        "confidence": result["confidence"],
        "input_text": input.text
    }