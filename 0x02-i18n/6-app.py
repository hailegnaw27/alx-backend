#!/usr/bin/env python3
"""
This module contains a Flask app with Babel for i18n support.
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, _


class Config:
    """Config class for Flask app."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)

# Mock user table
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user(user_id: int) -> dict or None:
    """
    Get user details by user ID.

    Args:
        user_id (int): The ID of the user.

    Returns:
        dict or None: The user details dictionary if found, else None.
    """
    return users.get(user_id)


@babel.localeselector
def get_locale() -> str:
    """
    Determine the best match with supported languages or the user's preferred locale.

    Returns:
        str: The best match language code or the user's preferred locale.
    """
    user_locale = None
    if g.user:
        user_locale = g.user.get('locale')
        if user_locale in app.config['LANGUAGES']:
            return user_locale
    request_locale = request.args.get('locale')
    if request_locale in app.config['LANGUAGES']:
        return request_locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.before_request
def before_request() -> None:
    """
    Set the logged-in user globally on flask.g.user.
    """
    user_id = request.args.get('login_as')
    if user_id:
        g.user = get_user(int(user_id))
    else:
        g.user = None


@app.route('/')
def index() -> str:
    """
    The index route that renders an HTML template with a welcome message.

    Returns:
        str: The rendered HTML template as a string.
    """
    return render_template('6-index.html')


if __name__ == "__main__":
    app.run()
