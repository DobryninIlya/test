print(0)

try:
    from flask import Flask

    app = Flask(__name__)

    @app.route("/")
    def index():
        return "hello world"

    if __name__ == "__main__":
        port = int(os.environ.get("PORT", 5000))
        app.run("0.0.0.0", port=port, debug=True)
except Exception as e:
    print(e)
