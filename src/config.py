import os


class Config:
    BASE_URL = os.getenv('BASE_URL', 'http://localhost:5000')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///url_shortener.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
