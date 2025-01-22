import json

from openapi_spec_validator import validate
from fastapi.testclient import TestClient
import yaml

from app.main import app
from app.util import override_token

override_token("test_token")
client = TestClient(app)


def test_openapi_plain() -> None:
    response = client.get("/spec/openapi")
    assert response.status_code == 200
    spec = yaml.safe_load(response.text)
    validate(spec)


def test_yaml_valid() -> None:
    response = client.get("/spec/openapi.yaml")
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/x-yaml"
    spec = yaml.safe_load(response.text)
    validate(spec)


def test_json_valid() -> None:
    response = client.get("/spec/openapi.json")
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
    spec = json.loads(response.text)
    validate(spec)
