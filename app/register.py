from datetime import date
import time

from flask import g, request
from werkzeug.contrib.fixers import ProxyFix

from .blueprints.page import page
from .extensions import babel
from .lib.jinja.filters import datetime_filter, datetime_to_unix_timestamp


def middleware(app):
    """
    Register 0 or more middleware (mutates the app passed in).

    :param app: Flask application instance
    :return: None
    """
    # Swap request.remote_addr with the real IP address even if behind a proxy.
    app.wsgi_app = ProxyFix(app.wsgi_app)
    return None


def blueprints(app):
    """
    Register 0 or more blueprints (mutates the app passed in).

    :param app: Flask application instance
    :return: None
    """
    FLASK_BLUEPRINTS = [
        page
    ]
    for blueprint in FLASK_BLUEPRINTS:
        app.register_blueprint(blueprint)
    return None


def extensions(app):
    """
    Register 0 or more extensions (mutates the app passed in).

    :param app: Flask application instance
    :return: None
    """
    # Register extensions
    babel.init_app(app)
    return None


def jinja_extensions(app):
    # Enable Jinja2's do expression-statement
    app.jinja_env.add_extension('jinja2.ext.do')

    # Custom filters
    app.jinja_env.filters['datetime'] = datetime_filter
    app.jinja_env.filters['to_unix_timestamp'] = datetime_to_unix_timestamp

    # Custom global environment variables
    app.jinja_env.globals['get_year'] = lambda: date.today().year
    return None


def logging_handler(app):
    """
    Register 0 or more logger handles (mutates the app passed in).

    :param app: Flask application instance
    :return: None
    """


    @app.before_request
    def before_request():
        """
        Save time when the request started.

        :return: None
        """
        g.start = time.time()

        # Attempts to verify if request is behind a proxy.
        # Source: https://github.com/mattupstate/flask-security/blob/4049c0620383f42d37950c7a35af5ddd6df0540f/flask_security/utils.py#L65
        if 'X-Forwarded-For' in request.headers:
            remote_addr = request.headers.getlist('X-Forwarded-For')[0].split(',')[0]
        else:
            remote_addr = request.remote_addr or 'untrackable'
        g.remote_ip = remote_addr

        return None


    @app.after_request
    def after_request(response):
        """
        Write out a log entry for the request.

        :return: Flask response
        """
        if 'start' in g:
            response_time = (time.time() - g.start)
        else:
            response_time = 0

        response_time_in_ms = int(response_time * 1000)

        params = {
            'method': request.method,
            'in': response_time_in_ms,
            'url': request.path,
            'ip': request.remote_addr
        }

        app.logger.info('%(method)s "%(url)s" in %(in)sms for %(ip)s', params)

        return response