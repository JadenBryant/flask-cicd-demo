from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "<h1>🚀 Hello from Flask CI/CD Demo v2.2 \
        <p>This update to my repository was automatically deployed to my Railway site.</p>"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
