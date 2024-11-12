from flask import Flask, redirect, jsonify


app = Flask(__name__)


# Function for shortening URLs
def shorten_url():
    """
    Function to shorten a URL. You should also be able to update the expiration time of the shortened URL.
    Input: JSON 
    {
        "id": 1, // Optional, if provided, update the expiration time of the shortened URL
        "url": "http://example.com",
        "custom_expiration": {
            "type": "DAY", // Type could be SECOND, MINUTE, HOUR, DAY, WEEK, MONTH, YEAR
            "value": 1
        } 
    }
    Output: Shortened URL
    """
    # Your code here
    short_url = '<-- Your code here -->'

    return jsonify({
        "id": 1,
        "url": "http://example.com",
        "custom_expiration": {
            "type": "DAY",
            "value": 1
        },
        "short_url": short_url
    }), 200


# Route for redirection
def redirect_url(short_url):
    """
    Redirect to the original URL using the short URL.
    """
    # Your code here
    original_url = '<-- Your code here -->'

    return redirect(original_url)


# Route for getting analytics
def url_analytics(short_url):
    """
    Get analytics for a shortened URL.
    Output: Usage statistics
    Feel free to have fun with this response. You can include any information you think is relevant.
    Response: {
        "original_url": "https://example.com",
        "short_url": "http://localhost:5000/abc123",
        "access_count": 12,
        "expiration_time": "2021-08-01 12:00:00"
    }
    """
    # Get your analytics data here
    return jsonify({
        "original_url": "https://example.com",
        "short_url": "http://localhost:5000/abc123",
        "access_count": 12,
        "expiration_time": "2021-08-01 12:00:00"
    }), 200
