from flask import Flask
from .extensions import db
from .config import Config
from .resources import shorten_url, redirect_url, url_analytics

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

with app.app_context():
    db.create_all()

# Register routes without Flask-RESTful
app.add_url_rule('/shorten', view_func=shorten_url, methods=['POST'])
app.add_url_rule('/<string:short_url>', view_func=redirect_url)
app.add_url_rule('/analytics/<string:short_url>', view_func=url_analytics)
