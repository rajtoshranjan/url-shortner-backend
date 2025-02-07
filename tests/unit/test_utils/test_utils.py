import pytest
from datetime import datetime, UTC

from src.utils import calculate_expiration_time


@pytest.mark.parametrize("exp_type, value", [
    ('SECOND', 30),
    ('MINUTE', 5),
    ('HOUR', 2),
    ('DAY', 1),
    ('WEEK', 1),
    ('MONTH', 1),
    ('YEAR', 1)
])
def test_calculate_expiration_time_with_valid_types(exp_type, value):
    """
    Test calculating expiration time with all valid types
    """

    # Arrange
    before = datetime.now(UTC)

    # Act
    expiration = calculate_expiration_time(exp_type, value)

    # Assert
    assert expiration > before
    assert isinstance(expiration, datetime)
    assert expiration.tzinfo == UTC


def test_calculate_expiration_time_invalid_type():
    """
    Test calculating expiration time with invalid type raises ValueError
    """

    with pytest.raises(ValueError) as exc_info:
        calculate_expiration_time('INVALID', 1)

    assert 'Invalid expiration type: INVALID' in str(exc_info.value)
