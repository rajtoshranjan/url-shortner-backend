import json

from src.api import app


def test_analytics_success(client, sample_url):
    """
    Test successful retrieval of URL analytics
    """
    # Arrange
    for _ in range(3):
        client.get(f'/{sample_url.short_url}')

    # Act
    analytics_response = client.get(f'/analytics/{sample_url.short_url}')
    analytics_data = json.loads(analytics_response.data)

    # Assert
    assert analytics_response.status_code == 200
    assert analytics_data['original_url'] == sample_url.original_url
    assert analytics_data['access_count'] == 3
    assert analytics_data['short_url'] == f"{app.config['BASE_URL']}/{sample_url.short_url}"


def test_analytics_nonexistent_url(client):
    """
    Test analytics for non-existent short URL
    """
    # Arrange
    nonexistent_url = 'nonexistent'

    # Act
    response = client.get(f'/analytics/{nonexistent_url}')

    # Assert
    assert response.status_code == 404


def test_analytics_with_expiration(client, url_with_expiry):
    """
    Test analytics for URL with expiration time
    """
    # Act
    analytics_response = client.get(f'/analytics/{url_with_expiry.short_url}')
    analytics_data = json.loads(analytics_response.data)

    # Assert
    assert analytics_response.status_code == 200
    assert analytics_data['expiration_time'] is not None


def test_analytics_zero_access_count(client, sample_url):
    """
    Test analytics for URL that hasn't been accessed
    """
    # Act
    analytics_response = client.get(f'/analytics/{sample_url.short_url}')
    analytics_data = json.loads(analytics_response.data)

    # Assert
    assert analytics_response.status_code == 200
    assert analytics_data['access_count'] == 0
