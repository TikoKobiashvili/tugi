from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_sentiment_analysis():
    response = client.post("/ai/sentiment", json={"text": "This is a test."})
    assert response.status_code == 200
    assert response.json()["sentiment"] in ["positive", "negative", "neutral"]
