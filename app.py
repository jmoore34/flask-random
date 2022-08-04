"""
A small flask application.
Run `flask run` in the directory to start.
"""

import os
from random import randint, random
from flask import Flask, Response

app = Flask(__name__)
app.secret_key = "1ccbfc0a11ac4264b771d230fb952b95"


@app.route("/")
def home() -> Response:
    return """
    <h1>Flask Random Service</h1>
    <p>Endpoints:</p>
    <ul>
        <li>/int/&lt;min&gt;/&lt;max&gt;</li>
        <li>/coin</li>
    """

@app.route("/int/<int:min>/<int:max>")
def int_range(min, max):
    return str(randint(min, max))

@app.route("/coin")
def coin_flip():
    if random() < 0.5:
        return "Heads"
    return "Tails"


if __name__ == "__main__":
    if os.environ.get("FLASK_ENV") == "production":
        from waitress import serve
        serve(app, host="0.0.0.0", port=80)
    else: # development
        app.run()
