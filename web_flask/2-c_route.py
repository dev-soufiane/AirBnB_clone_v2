#!/usr/bin/python3
"""This module starts a Flask web application;"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_holberton():
    """Function that returns a string at the root route."""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Function returns a string at the /hbnb route."""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
    """Function that returns a string at the /c/<text> route,
    expands the <text> variable."""
    new = text.replace('_', ' ')
    return 'C %s' % new


if __name__ == '__main__':
    app.run(host='0.0.0.0')
