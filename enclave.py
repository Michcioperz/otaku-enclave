#!/usr/bin/env python3
import council, protector, render_template
from flask import Flask

app = Flask(__name__)
app.config["DEBUG"] = True

def storages():
    return [protector.Storage(data) for data in council.STORAGES]

def all_shows():
    shows = []
    for storage in storages():
        shows += storage.shows()
    return shows

@app.route("/")
def home():
    return render_template("home.html", shows=all_shows())

if __name__ == '__main__':
    app.run(port=8766)
