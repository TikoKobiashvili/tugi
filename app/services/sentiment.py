import random

from app.schema import Sentiment


def analyze_sentiment(text: str) -> Sentiment:
    """Mock sentiment analysis logic."""
    return random.choice(list(Sentiment))
