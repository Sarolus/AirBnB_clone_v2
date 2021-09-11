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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
