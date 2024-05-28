#!/usr/bin/env python3
"""
Flask app to demonstrate i18n with forced locale via URL parameter
"""
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    """Configuration for Flask app with Babel."""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """Determine the best match for supported languages."""
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """Render the index page."""
    return render_template('4-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
