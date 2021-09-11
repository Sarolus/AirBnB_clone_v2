#!/usr/bin/python3
"""
    Script that starts a Flask web application.
"""
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def home():
    """
        Display a string on home.
    """
    return "Hello HBNB!"


@app.route("/hbnb")
def HBNB():
    """
        Display a string on /hbnb.
    """
    return "HBNB"


@app.route("/c/<text>")
def C(text):
    """
        Display a specified string on /c/.
    """
    return("C " + text.replace("_", " "))


@app.route("/python", defaults={'text': "is cool"})
@app.route("/python/<text>")
def python(text):
    """
        Display a specified string otherwise a default string
        on /python/.
    """
    return ("Python " + text.replace("_", " "))


@app.route("/number/<int:n>")
def number(n):
    """
        Display n on /number/ only if it's an integer.
    """
    return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
