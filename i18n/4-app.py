#!/usr/bin/env python3
"""Force locale with URL parameter"""

from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """App configuration for Babel"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)


def get_locale():
    """Get the best matching language from URL or headers"""
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


babel = Babel(app, locale_selector=get_locale)


@app.route('/')
def index():
    """Render the index page"""
    return render_template('4-index.html')


if __name__ == "__main__":
    app.run()
