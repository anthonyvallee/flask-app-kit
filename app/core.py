from flask import Flask
from .register import (blueprints,
                       extensions,
                       jinja_extensions,
                       logging_handler,
                       middleware)

def create_app(settings_override=None):
    """
    Create a Flask application using the app factory pattern.

    :param settings_override: Override settings
    :return: Flask app
    """
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('config.settings')
    app.config.from_pyfile('settings.py', silent=True)

    if settings_override:
        app.config.update(settings_override)

    blueprints(app)
    extensions(app)
    jinja_extensions(app)
    logging_handler(app)
    middleware(app)
    return app


