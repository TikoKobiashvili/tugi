from fastapi import APIRouter, Depends
from fastapi.security import HTTPAuthorizationCredentials

from app.schema import AsyncTaskRequest, AsyncTaskResponse
from app.schema import SentimentRequest, SentimentResponse
from app.services.async_task import perform_async_task
from app.services.sentiment import analyze_sentiment
from app.util import verify_token

router = APIRouter()


@router.post("/ai/sentiment", response_model=SentimentResponse, tags=["ai"], summary="Analyze sentiment")
async def sentiment_analysis(request: SentimentRequest,
                             credentials: HTTPAuthorizationCredentials = Depends(verify_token),
                             ) -> SentimentResponse:
    """Endpoint to analyze sentiment of the given text."""
    sentiment = analyze_sentiment(request.text)
    return SentimentResponse(sentiment=sentiment)


@router.post("/ai/async-task", response_model=AsyncTaskResponse, tags=["ai"], summary="Perform asynchronous task")
async def async_task(request: AsyncTaskRequest,
                     credentials: HTTPAuthorizationCredentials = Depends(verify_token)) -> AsyncTaskResponse:
    """Endpoint to perform an asynchronous task with the given number."""
    result = await perform_async_task(request.number)
    return AsyncTaskResponse(result=result)
