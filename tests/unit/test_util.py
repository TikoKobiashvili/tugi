import pytest

from app.util import require_value, require_condition


def test_requirements() -> None:
    assert require_value(1) == 1
    require_condition(True)

    with pytest.raises(AssertionError):
        require_condition(False)

    with pytest.raises(ValueError):
        require_value(None)
