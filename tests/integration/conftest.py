import logging
import pytest
from datetime import datetime, timedelta, UTC

from flask.testing import FlaskClient
from sqlalchemy.orm import Session
from src.api import app
from src.extensions import db
from src.models import URL


logger = logging.getLogger(__name__)


@pytest.fixture(scope="session", autouse=True)
def setup_test_db():
    """
    Create test database tables once for all tests
    """

    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'

    logger.info("Setting up test database...")
    with app.app_context():
        db.create_all()
        logger.info("Test database tables created")
        yield
        db.drop_all()
        logger.info("Test database cleaned up")


@pytest.fixture(autouse=True)
def setup_test_session(setup_test_db):
    """
    Create a clean session for each test
    """

    with app.app_context():
        yield
        db.session.rollback()
        db.session.remove()


@pytest.fixture
def client() -> FlaskClient:
    """
    Create a test client for the app
    """
    return app.test_client()


@pytest.fixture
def session() -> Session:
    """
    Create a new database session for each test
    """
    return db.session


@pytest.fixture
def sample_url(session: Session) -> URL:
    """
    Create a sample URL directly using the model
    """
    url = URL(
        original_url='http://example.com',
        short_url=URL.generate_short_url()
    )
    session.add(url)
    session.commit()
    session.refresh(url)
    return url


@pytest.fixture
def expired_url(session: Session) -> URL:
    """
    Create an URL with 1 second expiration directly using the model
    """
    url = URL(
        original_url='http://example.com',
        short_url=URL.generate_short_url(),
        expiration_time=datetime.now(UTC) - timedelta(seconds=1)
    )
    session.add(url)
    session.commit()
    session.refresh(url)
    return url


@pytest.fixture
def url_with_expiry(session: Session) -> URL:
    """
    Create a URL with 1 day expiration directly using the model
    """
    url = URL(
        original_url='http://example.com',
        short_url=URL.generate_short_url(),
        expiration_time=datetime.now(UTC) + timedelta(days=1)
    )
    session.add(url)
    session.commit()
    session.refresh(url)
    return url
