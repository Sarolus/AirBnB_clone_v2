#!/usr/bin/python3
"""
    Script that starts a Flask web application.
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown_db(self):
    """
        Tear down database
    """
    storage.close()


@app.route("/cities_by_states")
def states_list():
    """
        Display 8-states_list.html template on /cities_by_states
    """
    states = storage.all(State).values()
    return render_template("8-cities_by_states.html", states=states)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
