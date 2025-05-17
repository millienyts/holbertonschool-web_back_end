#!/usr/bin/env python3
"""Use user locale preference if available"""

from flask import Flask, render_template, request, g
from flask_babel import Babel


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
    """Select best language following priority rules"""
    url_locale = request.args.get("locale")
    if url_locale in app.config["LANGUAGES"]:
        return url_locale

    user = g.get('user', None)
    if user:
        user_locale = user.get("locale")
        if user_locale in app.config["LANGUAGES"]:
            return user_locale

    return request.accept_languages.best_match(app.config["LANGUAGES"])


babel = Babel(app, locale_selector=get_locale)


def get_user():
    """Return user dict based on login_as query param"""
    try:
        user_id = int(request.args.get("login_as"))
        return users.get(user_id)
    except Exception:
        return None


@app.before_request
def before_request():
    """Store user in Flask global context"""
    g.user = get_user()


@app.route('/')
def index():
    """Render index page"""
    return render_template('6-index.html')


if __name__ == "__main__":
    app.run()
