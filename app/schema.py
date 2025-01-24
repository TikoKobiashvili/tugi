from enum import Enum
from pydantic import BaseModel


class Sentiment(str, Enum):
    positive = "positive"
    negative = "negative"
    neutral = "neutral"


class SentimentRequest(BaseModel):
    text: str


class SentimentResponse(BaseModel):
    sentiment: Sentiment
