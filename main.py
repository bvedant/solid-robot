from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI()

sentiment_pipeline = pipeline("sentiment-analysis")

class Text(BaseModel):
    text: str

@app.post("/analyze")
def analyze_sentiment(input: Text):
    result = sentiment_pipeline(input.text)
    return result
