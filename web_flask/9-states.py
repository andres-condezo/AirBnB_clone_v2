#!/usr/bin/python3
"""This module starts a flask app on 0.0.0.0:5000"""

from models import storage
from flask import Flask, abort, render_template
app = Flask(__name__)


@app.teardown_appcontext
def tear_down(exception):
    storage.close()


@app.route('/states', strict_slashes=False)
def states():
    """Renders an HTML page"""
    states = storage.all("State")
    return render_template('9-states.html', states=states)


@app.route('/states/<_id>', strict_slashes=False)
def state(_id):
    """Renders an HTML page"""
    states = storage.all("State")
    state = None
    for st in states.values():
        if _id == st.id:
            state = st
            break
    return render_template('9-states.html', state=state)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
