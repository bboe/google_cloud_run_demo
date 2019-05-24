import time

from flask import Flask


app = Flask(__name__)


@app.route("/<name>")
def hello(name):
    time.sleep(3)
    return f"Hello {name}"
