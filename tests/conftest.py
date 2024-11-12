import pytest
from src.api import app


@pytest.fixture
def client():
    """A test client for the app."""
    return app.test_client()