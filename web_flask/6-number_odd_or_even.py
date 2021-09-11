#!/usr/bin/python3
"""
    Script that starts a Flask web application.
"""
from flask import Flask, render_template

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


@app.route("/number_template/<int:n>")
def number_template(n):
    """
        Display 5-number.html template on /number_template/.
    """
    return render_template("5-number.html", number=n)


@app.route("/number_odd_or_even/<int:n>")
def number_odd_or_even(n):
    """
        Display 6-number_odd_or_even.html template on /number_odd_or_even/.
    """
    return render_template("6-number_odd_or_even.html", number=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
