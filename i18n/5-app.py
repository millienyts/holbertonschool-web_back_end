#!/usr/bin/env python3
"""Mock login and localize user message"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, gettext


class Config:
    """App configuration"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


app = Flask(__name__)
app.config.from_object(Config)


def get_locale():
    """Determine best locale from user or request"""
    user = g.get('user', None)
    if user and user.get('locale') in app.config['LANGUAGES']:
        return user.get('locale')

    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale

    return request.accept_languages.best_match(app.config['LANGUAGES'])


babel = Babel(app, locale_selector=get_locale)


def get_user():
    """Return a user dictionary or None"""
    try:
        user_id = int(request.args.get('login_as'))
        return users.get(user_id)
    except Exception:
        return None


@app.before_request
def before_request():
    """Set user in global context"""
    g.user = get_user()


@app.route('/')
def index():
    """Render the index page"""
    return render_template('5-index.html')


if __name__ == "__main__":
    app.run()
