import json


def test_redirect_success(client, sample_url):
    """
    Test successful redirection to original URL
    """

    # Act
    redirect_response = client.get(f'/{sample_url.slug}')

    # Assert
    assert redirect_response.status_code == 302
    assert redirect_response.headers['Location'] == sample_url.original_url


def test_redirect_nonexistent_url(client):
    """
    Test redirection for non-existent URL slug
    """

    # Arrange
    nonexistent_slug = 'nonexistent'

    # Act
    response = client.get(f'/{nonexistent_slug}')

    # Assert
    assert response.status_code == 404


def test_redirect_expired_url(client, expired_url):
    """
    Test redirection for expired URL
    """

    # Act
    redirect_response = client.get(f'/{expired_url.slug}')
    response_data = json.loads(redirect_response.data)

    # Assert
    assert redirect_response.status_code == 410
    assert response_data['error'] == 'URL has expired'


def test_redirect_increments_access_count(client, sample_url):
    """
    Test that access count increments on redirection
    """

    # Act
    for _ in range(3):
        client.get(f'/{sample_url.slug}')

    analytics_response = client.get(f'/analytics/{sample_url.slug}')
    analytics_data = json.loads(analytics_response.data)

    # Assert
    assert analytics_response.status_code == 200
    assert analytics_data['access_count'] == 3
