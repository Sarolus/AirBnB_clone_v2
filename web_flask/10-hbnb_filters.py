#!/usr/bin/python3
"""
    Script that starts a Flask web application.
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown_db(self):
    """
        Tear down database
    """
    storage.close()


@app.route("/hbnb_filters")
def filters():
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    return render_template(
        "10-hbnb_filters.html",
        **locals()
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
