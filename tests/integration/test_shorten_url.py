import json


def test_shorten_url_success(client):
    """
    Test successful URL shortening
    """
    # Arrange
    payload = {
        'url': 'http://example.com',
        'custom_expiration': {
            'type': 'DAY',
            'value': 1
        }
    }

    # Act
    response = client.post('/shorten', json=payload)
    data = json.loads(response.data)

    # Assert
    assert response.status_code == 201
    assert 'id' in data
    assert data['url'] == 'http://example.com'
    assert 'short_url' in data
    assert data['custom_expiration']['type'] == 'DAY'
    assert data['custom_expiration']['value'] == 1


def test_shorten_url_missing_url(client):
    """
    Test error when URL is missing
    """
    # Arrange
    payload = {}

    # Act
    response = client.post('/shorten', json=payload)
    data = json.loads(response.data)

    # Assert
    assert response.status_code == 400
    assert data['error'] == 'URL is required'


def test_shorten_url_invalid_expiration(client):
    """
    Test error when expiration type is invalid
    """
    # Arrange
    payload = {
        'url': 'http://example.com',
        'custom_expiration': {
            'type': 'INVALID',
            'value': 1
        }
    }

    # Act
    response = client.post('/shorten', json=payload)
    data = json.loads(response.data)

    # Assert
    assert response.status_code == 400
    assert 'Invalid expiration type' in data['error']


def test_update_url_expiration(client, sample_url):
    """
    Test updating expiration time of existing URL
    """
    # Arrange
    update_payload = {
        'id': sample_url.id,
        'url': sample_url.original_url,
        'custom_expiration': {
            'type': 'HOUR',
            'value': 20
        }
    }

    # Act
    update_response = client.post('/shorten', json=update_payload)
    update_data = json.loads(update_response.data)

    # Assert
    assert update_response.status_code == 200
    assert update_data['id'] == sample_url.id
    assert update_data['custom_expiration']['type'] == 'HOUR'
    assert update_data['custom_expiration']['value'] == 20


def test_update_nonexistent_url(client):
    """
    Test updating a URL that doesn't exist
    """
    # Arrange
    payload = {
        'id': 99999,
        'url': 'http://example.com',
        'custom_expiration': {
            'type': 'HOUR',
            'value': 2
        }
    }

    # Act
    response = client.post('/shorten', json=payload)
    data = json.loads(response.data)

    # Assert
    assert response.status_code == 404
    assert data['error'] == 'URL not found'


def test_shorten_url_generation_failure(client, monkeypatch):
    """
    Test error handling when short URL generation fails
    """

    # Arrange
    def mock_generate_short_url():
        raise ValueError("Could not generate unique short URL after multiple attempts")

    monkeypatch.setattr('src.models.URL.generate_short_url', mock_generate_short_url)

    payload = {
        'url': 'http://example.com'
    }

    # Act
    response = client.post('/shorten', json=payload)
    data = json.loads(response.data)

    # Assert
    assert response.status_code == 400
    assert data['error'] == "Could not generate unique short URL after multiple attempts"
