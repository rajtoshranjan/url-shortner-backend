import string

from datetime import datetime, UTC
from nanoid import generate
from .extensions import db


class URL(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(2048), nullable=False)
    short_url = db.Column(db.String(8), unique=True, nullable=False, index=True)
    created_at = db.Column(db.DateTime, default=datetime.now(UTC))
    expiration_time = db.Column(db.DateTime, nullable=True)
    access_count = db.Column(db.Integer, default=0)

    @staticmethod
    def generate_short_url():
        """
        Generate a random unique slug for the URL.

        Returns:
            str: A unique random short URL slug

        Raises:
            ValueError: If unable to generate a unique short URL after MAX_ATTEMPTS
        """

        MAX_ATTEMPTS = 10
        chars = string.ascii_letters + string.digits

        # Try generating unique short URLs up to MAX_ATTEMPTS times
        # This handles potential collisions with existing URLs in the database
        for _ in range(MAX_ATTEMPTS):
            short_url = generate(chars, 8)
            # Check if short_url already exists in database
            if not URL.query.filter_by(short_url=short_url).first():
                return short_url

        raise ValueError("Could not generate unique short URL after multiple attempts")

    def __repr__(self):
        return f'<URL {self.short_url}>'
