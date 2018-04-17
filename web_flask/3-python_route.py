#!/usr/bin/python3
from flask import Flask
app = Flask(__name__)
app.debug = True
@app.route('/', strict_slashes=False)
def hello():
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def things(text=None):
    return "C " + text.replace("_", " ")

@app.route('/python/<text>', strict_slashes=False)
def python(text=''):
    if text is '':
        text = "is cool"
    return "Python " + text.replace("_", " ")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
