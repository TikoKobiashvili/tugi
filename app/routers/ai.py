from fastapi import APIRouter

from app.schema import SentimentRequest, SentimentResponse
from app.services.sentiment import analyze_sentiment

router = APIRouter()


@router.post("/ai/sentiment", response_model=SentimentResponse, tags=["ai"], summary="Analyze sentiment")
async def sentiment_analysis(request: SentimentRequest) -> SentimentResponse:
    """Endpoint to analyze sentiment of the given text."""
    sentiment = analyze_sentiment(request.text)
    return SentimentResponse(sentiment=sentiment)
