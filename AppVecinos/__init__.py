import os
from flask import Flask


def create_app(config=None):
    app = Flask(__name__)

    app.config["API_TOKEN"] = os.environ.get("API_TOKEN", "")
    if config:
        app.config.update(config)

    from .api import api_bp
    app.register_blueprint(api_bp)

    return app
