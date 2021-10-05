#!/usr/bin/python3
"""This module starts a flask app on 0.0.0.0:5000"""

from models import storage
from flask import Flask, abort, render_template
app = Flask(__name__)


@app.teardown_appcontext
def tear_down(exception):
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def states():
    """Renders an HTML page"""
    states = storage.all("State")
    amenities = storage.all("Amenity")
    return render_template('10-hbnb_filters.html', states=states, amenities=amenities)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
