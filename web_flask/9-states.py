#!/usr/bin/python3
"""This module starts a Flask web application."""

from models import storage
from models.state import State
from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states_1(id=None):
    """Function that returns a rendered html template:
    if id is given, list the cities of that State
    else, list all States.
    """
    states = storage.all('State')
    if id:
        key = '{}.{}'.format('State', id)
        if key in states:
            states = states[key]
        else:
            states = None
    else:
        states = storage.all('State').values()
    return render_template('9-states.html', states=states, id=id)


@app.teardown_appcontext
def teardown(self):
    """Function that removes the current SQLAlchemy Session."""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0')
