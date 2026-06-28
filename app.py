from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello, World! Welcome to Flask 🚀"


@app.route("/health")
def health():
    return {
        "status": "healthy",
        "service": "Flask App"
    }


@app.route("/about")
def about():
    return "This is a basic Flask application."


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)