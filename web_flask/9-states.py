#!/usr/bin/python3
"""
    Script that starts a Flask web application.
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown_db(self):
    """
        Tear down database
    """
    storage.close()


@app.route("/states")
def states_list():
    """
        Display 7-states_list.html template on /states_list
    """
    states = storage.all(State).values()
    return render_template("7-states_list.html", states=states)


@app.route("/states/<string:id>")
def state(id):
    """
        Display all cities from a specified state from 9-states.html
        template on /states/
    """
    state = storage.all(State)
    key = "{}.{}".format("State", id)
    if key in state:
        value = state[key]
    else:
        value = None
    return render_template("9-states.html", state=value)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
