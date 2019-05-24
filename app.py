import time

from flask import Flask


app = Flask(__name__)


@app.route("/<name>")
def hello(name):
    time.sleep(3)
    if name == "0":
        name = "Mischa"
    return f"Hello {name}\n"
