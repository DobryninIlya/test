print(0)

try:
    from flask import Flask

    app = Flask(__name__)

    @app.route("/")
    def index():
        return "hello world"

    if __name__ == "__main__":
        app.run("0.0.0.0", port=80)
except Exception as e:
    print(e)
