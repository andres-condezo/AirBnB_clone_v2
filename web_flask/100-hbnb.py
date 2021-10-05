#!/usr/bin/python3
"""This module starts a flask app on 0.0.0.0:5000"""

from models import storage
from flask import Flask, abort, render_template
app = Flask(__name__)


@app.teardown_appcontext
def tear_down(exception):
    storage.close()


@app.route('/hbnb', strict_slashes=False)
def states():
    """Renders an HTML page"""
    s = storage.all("State")
    a = storage.all("Amenity")
    p = storage.all("Place")
    return render_template('100-hbnb.html', _states=s, _amenities=a, _places=p)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
