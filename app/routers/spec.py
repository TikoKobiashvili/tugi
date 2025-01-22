from typing import Any

from fastapi import APIRouter, status
from fastapi import FastAPI
from fastapi.responses import JSONResponse, PlainTextResponse
import yaml

router = APIRouter()
spec: dict[str, Any] = {}  # This will be set in register_router


class YAMLResponse(PlainTextResponse):
    media_type = "application/x-yaml"

    def render(self, content: Any) -> bytes:
        return yaml.dump(content).encode("utf-8")


@router.get(
    "/spec/openapi.json",
    tags=["openapi"],
    summary="Download JSON",
    description="Download spec in JSON format",
    status_code=status.HTTP_200_OK,
    response_model=str,
    operation_id="openApiJson",
)
def openapi_json() -> JSONResponse:
    return JSONResponse(content=spec)


@router.get(
    "/spec/openapi.yaml",
    tags=["openapi"],
    summary="Download YAML",
    description="Download spec in YAML format",
    status_code=status.HTTP_200_OK,
    response_model=str,
    operation_id="openApiYaml",
)
def openapi_yaml() -> YAMLResponse:
    return YAMLResponse(content=spec)


@router.get(
    "/spec/openapi",
    tags=["openapi"],
    summary="View YAML",
    description="View spec in YAML format (plain text mime type)",
    status_code=status.HTTP_200_OK,
    response_model=str,
    operation_id="openApiYamlPlainText",
)
def openapi_yaml_plain() -> PlainTextResponse:
    return PlainTextResponse(content=yaml.dump(spec).encode("utf-8"))


def register_router(app: FastAPI) -> None:
    global spec
    app.include_router(router)
    spec = app.openapi()
    spec["servers"] = [
        {
            "url": "http://localhost:8041",
            "description": "Local development server",
        }
    ]
    spec["tags"] = [
        {
            "name": "healthcheck",
            "description": "Operations related to the health check endpoint",
        },
        {
            "name": "openapi",
            "description": "Operations related to the OpenAPI specification",
        },
    ]
    spec["info"]["contact"] = {
        "name": "Tugi Tark",
        "url": "https://tugitark.com",
    }
    spec["info"]["description"] = "API for the test service"
