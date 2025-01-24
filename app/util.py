import os
from dotenv import load_dotenv
from typing import Optional, TypeVar

from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import Depends, HTTPException, status


load_dotenv()


TOKEN_VAR = "AI_SERVICE_API_KEY"  # nosec
security = HTTPBearer()
token: Optional[str] = None


def require_env(var_name: str) -> str:
    """Require an environment variable, or raise an exception if it does not exist or is empty."""
    value = os.getenv(var_name)
    if not value:
        raise EnvironmentError(f"The environment variable '{var_name}' is not set or is empty.")
    return value


def override_token(new_token: Optional[str]) -> None:
    global token
    token = new_token


def get_token() -> str:
    global token
    if token is None:
        token = require_env(TOKEN_VAR)
    if not token:
        raise EnvironmentError("The token is not set or is empty.")
    return token


async def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)) -> None:
    if credentials.credentials != get_token():
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
            headers={"WWW-Authenticate": "Bearer"},
        )


def require_condition(condition: bool, message: Optional[str] = None) -> None:
    if not condition:
        raise AssertionError(message or "Condition failed")


T = TypeVar("T")


def require_value(value: Optional[T], message: Optional[str] = None) -> T:
    if value is None:
        raise ValueError(message or "Value is None")
    return value
