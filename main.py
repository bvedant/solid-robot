from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import pipeline, AutoModelForSequenceClassification, AutoTokenizer
import os

app = FastAPI()

MODEL_NAME = os.getenv("MODEL_NAME", "distilbert-base-uncased-finetuned-sst-2-english")
REVISION = os.getenv("REVISION", "main")

model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME, revision=REVISION)
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, revision=REVISION)
sentiment_pipeline = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)

class Text(BaseModel):
    text: str

@app.post("/analyze")
def analyze_sentiment(input: Text):
    try:
        result = sentiment_pipeline(input.text)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
def health():
    return {"status": "ok"}
