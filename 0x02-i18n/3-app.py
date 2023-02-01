#!/usr/bin/env python3
""" Module to Parametrize templates"""

from flask import Flask, render_template, request
from flask_babel import Babel, _


class Config(object):
    """config for babel"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)

# Load babel
app.config.from_object(Config)


def get_locale():
    """ Get locale from request"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


babel = Babel(app)


@app.route('/')
def index():
    """ view function to load 1-index.html"""
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0', debug=True)