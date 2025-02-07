from flask import request, current_app
from datetime import datetime, UTC, timedelta
from typing import Literal


def calculate_expiration_time(
    expiration_type: Literal[
        'SECOND', 'MINUTE', 'HOUR', 'DAY', 'WEEK', 'MONTH', 'YEAR'
    ],
    value: int
) -> datetime:
    """
    Calculate expiration time based on type and value

    Args:
        expiration_type: The type of expiration
        value: The value of the expiration

    Returns:
        datetime: The expiration time
    """

    time_deltas = {
        'SECOND': timedelta(seconds=value),
        'MINUTE': timedelta(minutes=value),
        'HOUR': timedelta(hours=value),
        'DAY': timedelta(days=value),
        'WEEK': timedelta(weeks=value),
        'MONTH': timedelta(days=value * 30),
        'YEAR': timedelta(days=value * 365)
    }

    if expiration_type not in time_deltas:
        raise ValueError(f"Invalid expiration type: {expiration_type}")

    return datetime.now(UTC) + time_deltas[expiration_type]


def get_base_url() -> str:
    """
    Returns base URL of the app
    """

    if base_url := current_app.config.get('BASE_URL'):
        return base_url

    return request.host_url.rstrip('/')
