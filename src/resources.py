from flask import (
    Flask, redirect, jsonify, request, abort, Response
)
from datetime import datetime, UTC
from .models import URL
from .extensions import db
from .utils import calculate_expiration_time, get_base_url

app = Flask(__name__)


# Function for shortening URLs
def shorten_url():
    """
    Function to shorten a URL or update expiration time
    """

    data = request.get_json()

    if not data or 'url' not in data:
        return jsonify({'error': 'URL is required'}), 400

    # If ID is provided, update existing URL
    if id := data.get('id'):
        url_entry = URL.query.get(id)
        if not url_entry:
            return jsonify({'error': 'URL not found'}), 404

        if custom_expiration := data.get('custom_expiration'):
            try:
                url_entry.expiration_time = calculate_expiration_time(
                    custom_expiration['type'],
                    custom_expiration['value']
                )
                db.session.commit()
            except ValueError as e:
                return jsonify({'error': str(e)}), 400

        return jsonify({
            'id': url_entry.id,
            'url': url_entry.original_url,
            'custom_expiration': {
                'type': data.get('custom_expiration', {}).get('type'),
                'value': data.get('custom_expiration', {}).get('value')
            },
            'short_url': f"{get_base_url()}/{url_entry.short_url}"
        }), 200

    # Generate a unique short URL.
    try:
        slug = URL.generate_short_url()
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

    # Create new shortened URL
    url_entry = URL(
        original_url=data['url'],
        short_url=slug
    )

    if 'custom_expiration' in data:
        try:
            url_entry.expiration_time = calculate_expiration_time(
                data['custom_expiration']['type'],
                data['custom_expiration']['value']
            )
        except ValueError as e:
            return jsonify({'error': str(e)}), 400

    db.session.add(url_entry)
    db.session.commit()

    return jsonify({
        'id': url_entry.id,
        'url': url_entry.original_url,
        'custom_expiration': data.get('custom_expiration'),
        'short_url': f"{get_base_url()}/{url_entry.short_url}"
    }), 201


# Route for redirection
def redirect_url(short_url: str) -> Response:
    """Redirect to the original URL"""
    url_entry = URL.query.filter_by(short_url=short_url).first()

    if not url_entry:
        abort(404)

    if url_entry.expiration_time:
        url_expiration_time = url_entry.expiration_time.replace(tzinfo=UTC)
        current_time = datetime.now(UTC)

        if current_time > url_expiration_time:
            return jsonify({'error': 'URL has expired'}), 410

    url_entry.access_count += 1
    db.session.commit()

    return redirect(url_entry.original_url)


# Route for getting analytics
def url_analytics(short_url: str) -> Response:
    """Get analytics for a shortened URL"""
    url_entry = URL.query.filter_by(short_url=short_url).first()

    if not url_entry:
        abort(404)

    base_url = get_base_url()
    expiration_time = url_entry.expiration_time.isoformat() if url_entry.expiration_time else None

    return jsonify({
        'original_url': url_entry.original_url,
        'short_url': f"{base_url}/{url_entry.short_url}",
        'access_count': url_entry.access_count,
        'expiration_time': expiration_time
    }), 200
