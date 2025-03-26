import os

from flask import Flask, render_template, send_from_directory, url_for

app = Flask(__name__)


@app.route("/download")
def download_cv():
    return send_from_directory("downloads", "CV_Sergio_Monsalve.pdf", as_attachment=True)

@app.route("/cv")
def cv():
    return render_template("cv.html")

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/hi")
def hello_world():
    """Example Hello World route."""
    name = os.environ.get("NAME", "World")
    return f"Hello {name}!"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))