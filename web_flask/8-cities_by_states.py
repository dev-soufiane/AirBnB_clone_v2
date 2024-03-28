#!/usr/bin/python3
"""This module starts a Flask web application."""

from models import storage
from models.state import State
from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities():
    """Function that returns a rendered html template
    at the /cities_by_states route,
    listing the cities by states."""
    return render_template('8-cities_by_states.html',
                           states=storage.all('State').values())


@app.teardown_appcontext
def teardown(self):
    """Function that removes the current SQLAlchemy Session."""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0')
