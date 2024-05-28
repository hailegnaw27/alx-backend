#!/usr/bin/env python3
"""
Flask app to display the current time
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, _, get_timezone
from datetime import datetime
import pytz

app = Flask(__name__)
babel = Babel(app)


class Config:
    """Configuration for Flask app with Babel."""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user(user_id: int):
    """Get a user by ID."""
    return users.get(user_id)


@app.before_request
def before_request():
    """Set the user in the global context before each request."""
    user_id = request.args.get('login_as')
    if user_id:
        g.user = get_user(int(user_id))
    else:
        g.user = None


@babel.localeselector
def get_locale():
    """Determine the best match for supported languages."""
    # Locale from URL parameters
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale

    # Locale from user settings
    if g.user and g.user.get('locale') in app.config['LANGUAGES']:
        return g.user['locale']

    # Locale from request header
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone():
    """Determine the best match for supported time zones."""
    # Time zone from URL parameters
    tz = request.args.get('timezone')
    if tz:
        try:
            pytz.timezone(tz)
            return tz
        except pytz.exceptions.UnknownTimeZoneError:
            pass

    # Time zone from user settings
    if g.user and g.user.get('timezone'):
        try:
            pytz.timezone(g.user['timezone'])
            return g.user['timezone']
        except pytz.exceptions.UnknownTimeZoneError:
            pass

    # Default to UTC
    return 'UTC'


@app.route('/')
def index():
    """Render the index page."""
    current_time = datetime.now(pytz.timezone(get_timezone()))
    return render_template('index.html', current_time=current_time)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
