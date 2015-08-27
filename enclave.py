#!/usr/bin/env python3
import council, protector
from flask import Flask, render_template

app = Flask(__name__)
app.config["DEBUG"] = True


def all_shows():
    shows = []
    for storage in council.STORAGES:
        shows += storage.shows()
    return shows

def datafy_all_shows(shows=None):
    if shows is None:
        shows = all_shows()
    for show in shows:
        for provider in council.DATA_PROVIDERS:
            provider.show_datafy(show)
    return shows

@app.route("/")
def home():
    return render_template("home.html", shows=all_shows())

if __name__ == '__main__':
    app.run(port=8766)
