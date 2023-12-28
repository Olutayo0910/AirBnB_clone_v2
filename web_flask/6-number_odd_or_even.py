#!/usr/bin/python3
"""
Starts a Flask web application.
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB!'."""
    return 'Hello HBNB!'


@app.route('/', strict_slashes=False)
def hbnb():
    """Displays HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """ Displays “C ”, followed by the value of the text"""
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python', strict_slashes=False)
def c_python(text="is cool"):
    """Displays “Python ”, followed by the value of the text"""
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def c_number(n):
    """display “n is a number” only if n is an integer"""
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Displays a HTML page only if n is an integer"""
    return render_template('5-number.html', n=n)

@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_even(n):
    """Displays a HTML page only if n is an integer:"""
    div = 'odd'
    if n % 2 == 0:
        div = 'even'
    return render_template('6-number_odd_or_even.html', n=n, div=div)                             


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
