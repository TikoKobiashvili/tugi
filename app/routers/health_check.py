from typing import Literal

from fastapi import APIRouter, status, Depends
from fastapi.security import HTTPAuthorizationCredentials
from pydantic import BaseModel

from app.util import verify_token

router = APIRouter()


class DoHealthCheck(BaseModel):
    status: Literal["OK"]


class HealthCheck(BaseModel):
    status: str = "OK"


@router.get(
    "/health",
    tags=["healthcheck"],
    summary="Perform health check",
    description="Simple health check that returns HTTP status code 200",
    status_code=status.HTTP_200_OK,
    response_model=HealthCheck,
)
async def get_health() -> HealthCheck:
    return HealthCheck(status="OK")


@router.post(
    "/health",
    tags=["healthcheck"],
    summary="Perform health check with POST",
    description="Simple health check with POST that returns HTTP status code 200",
    status_code=status.HTTP_200_OK,
    response_model=HealthCheck,
)
async def post_health(request: DoHealthCheck) -> HealthCheck:
    return HealthCheck(status="OK")


@router.get(
    "/health-authenticated",
    tags=["healthcheck"],
    summary="Perform health check with authentication",
    description="Health check that returns HTTP status code 200 or 401 if the token is invalid",
    status_code=status.HTTP_200_OK,
    response_model=HealthCheck,
)
async def get_health_authenticated(
    credentials: HTTPAuthorizationCredentials = Depends(verify_token),
) -> HealthCheck:
    return HealthCheck(status="OK")
