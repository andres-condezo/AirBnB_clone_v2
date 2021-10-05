#!/usr/bin/python3
"""This module starts a flask app on 0.0.0.0:5000"""

from models import storage
from flask import Flask, abort, render_template
app = Flask(__name__)


@app.teardown_appcontext
def tear_down(exception):
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def main():
    """Renders an HTML page"""
    states = storage.all("State")
    return render_template('8-cities_by_states.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
