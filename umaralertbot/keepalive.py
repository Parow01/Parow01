from flask import Flask

def keep_alive():
    app = Flask(__name__)

    @app.route("/")
    def index():
        return "UmarAlertBot is active!"

    app.run(host="0.0.0.0", port=8080)
