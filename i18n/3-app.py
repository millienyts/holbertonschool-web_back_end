#!/usr/bin/env python3
"""Parametrize templates"""

from flask import Flask, render_template, request
from flask_babel import Babel, gettext


class Config:
    """App configuration for Babel"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)


def get_locale():
    """Determine the best match with supported languages"""
    return request.args.get('locale') if request.args.get('locale') in app.config['LANGUAGES'] \
        else request.accept_languages.best_match(app.config['LANGUAGES'])


babel = Babel(app, locale_selector=get_locale)


@app.route('/')
def index():
    """Render the index page"""
    return render_template('3-index.html')


if __name__ == "__main__":
    app.run()
