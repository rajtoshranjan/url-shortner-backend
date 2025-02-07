import pytest
from flask import Flask
from src.utils import get_base_url


@pytest.fixture
def app():
    """
    Create a Flask app for testing
    """

    app = Flask(__name__)
    app.config['BASE_URL'] = 'http://test.com'
    return app


def test_get_base_url_from_config(app):
    """
    Test getting base URL from config
    """

    with app.app_context():
        base_url = get_base_url()
        assert base_url == 'http://test.com'


def test_get_base_url_from_request(app):
    """
    Test getting base URL from request when config is none
    """

    app.config['BASE_URL'] = None
    with app.test_request_context('http://example.com/test'):
        base_url = get_base_url()
        assert base_url == 'http://example.com'


def test_get_base_url_no_config(app):
    """
    Test that get_base_url returns localhost when config is none
    """

    app.config['BASE_URL'] = None
    with app.test_request_context():
        base_url = get_base_url()
        assert base_url == 'http://localhost'
