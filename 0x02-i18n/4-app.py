#!/usr/bin/env python3
"""
This module contains a Flask app with Babel for i18n support.
"""

from flask import Flask, render_template, request
from flask_babel import Babel, _


class Config:
    """Config class for Flask app."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """
    Determine the best match with supported languages or the forced locale.

    Returns:
        str: The best match language code or forced locale.
    """
    forced_locale = request.args.get('locale')
    if forced_locale in app.config['LANGUAGES']:
        return forced_locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    """
    The index route that renders an HTML template with a welcome message.

    Returns:
        str: The rendered HTML template as a string.
    """
    return render_template('4-index.html')


if __name__ == "__main__":
    app.run()
