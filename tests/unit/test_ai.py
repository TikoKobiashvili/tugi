from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_sentiment_analysis():
    headers = {
        "Authorization": "Bearer test_token"
    }
    response = client.post("/ai/sentiment", json={"text": "test"}, headers=headers)
    assert response.status_code == 200
    assert response.json()["sentiment"] in ["positive", "negative", "neutral"]


def test_async_task():
    headers = {
        "Authorization": "Bearer test_token"
    }
    # Test valid input
    response = client.post("/ai/async-task", json={"number": 5}, headers=headers)
    assert response.status_code == 200
    assert response.json()["result"] == 10

    # Test invalid input (negative number)
    response = client.post("/ai/async-task", json={"number": -5}, headers=headers)
    assert response.status_code == 400
    assert response.json()["detail"] == "Number must be non-negative."
