from flask import Flask, render_template
from flask_cors import CORS

from backend.routes import api

app = Flask(__name__)

CORS(app)

app.register_blueprint(api)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/health")
def health():
    return {
        "status": "healthy"
    }


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )