from flask import Flask
from art import text2art
from time import sleep
import os


app = Flask(__name__)


@app.route("/")
def index():
    return text_render("200")


@app.route("/<text>")
def text(text):
    return text_render(text)


def text_render(text: str):
    yield "<pre>"
    for el in text2art(text, font='block', chr_ignore=True).split("\n"):

        for i in el:
            yield i
            sleep(0.005)
        yield "<br>"

    yield "</pre>"



if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run("0.0.0.0", port=port, debug=True)
