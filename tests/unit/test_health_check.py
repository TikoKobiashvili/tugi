from fastapi.testclient import TestClient

from app.main import app
from app.util import override_token

client = TestClient(app)


def test_get_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "OK"}


def test_post_health():
    response = client.post("/health", json={"status": "OK"})
    assert response.status_code == 200
    assert response.json() == {"status": "OK"}


def test_get_health_authenticated():
    override_token("test_token")

    headers = {
        "Authorization": "Bearer test_token"
    }
    response = client.get("/health-authenticated", headers=headers)
    assert response.status_code == 200
    assert response.json() == {"status": "OK"}


def test_get_health_authenticated_no_token():
    response = client.get("/health-authenticated")
    assert response.status_code == 403
    assert response.json() == {"detail": "Not authenticated"}


def test_get_health_authenticated_invalid_token():
    override_token("TEST")
    headers = {
        "Authorization": "Bearer invalid_token"
    }
    response = client.get("/health-authenticated", headers=headers)
    assert response.status_code == 401
    assert response.json() == {"detail": "Invalid token"}
