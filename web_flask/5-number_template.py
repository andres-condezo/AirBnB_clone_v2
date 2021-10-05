#!/usr/bin/python3
"""This module starts a flask app on 0.0.0.0:5000"""

from flask import Flask, abort, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def main():
    """Returns a text"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Returns HBNB"""
    return 'HBNB'


@app.route('/c/<txt>', strict_slashes=False)
def c_text(txt):
    """Returns a text passed as param"""
    return 'C {}'.format(txt.replace('_', ' '))


@app.route('/python/', strict_slashes=False)
@app.route('/python/<txt>', strict_slashes=False)
def py_text(txt='is cool'):
    """Returns a text passed as param"""
    return 'Python {}'.format(txt.replace('_', ' '))


@app.route('/number/<n>', strict_slashes=False)
def num(n):
    """Returns a text if 'n' is number, gives a 404 otherwise"""
    if not n.isnumeric():
        abort(404)
    return '{} is a number'.format(n)


@app.route('/number_template/<n>', strict_slashes=False)
def num_html(n):
    """Returns a text if 'n' is number, gives a 404 otherwise"""
    if not n.isnumeric():
        abort(404)
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
