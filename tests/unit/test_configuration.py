import pytest

from app.util import get_token, override_token, require_env


def test_valid_env() -> None:
    require_env("PATH")


def test_missing_env() -> None:
    with pytest.raises(EnvironmentError):
        require_env("MISSING_ENV_VAR_y71c32")


def test_invalid_token() -> None:
    override_token("")

    with pytest.raises(EnvironmentError):
        get_token()
