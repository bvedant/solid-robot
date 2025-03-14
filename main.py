from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI()

sentiment_pipeline = pipeline("sentiment-analysis")

class Text(BaseModel):
    text: str

@app.post("/analyze")
def analyze_sentiment(input: Text):
    try:
        result = sentiment_pipeline(input.text)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
