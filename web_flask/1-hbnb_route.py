#!/usr/bin/python3
"""This module starts a flask app on 0.0.0.0:5000"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def main():
    """Returns a text when / route is requested"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Returns a text when a route is requested"""
    return 'HBNB'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
