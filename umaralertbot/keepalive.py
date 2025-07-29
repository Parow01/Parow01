# keepalive.py

from flask import Flask
import threading

def keep_alive():
    app = Flask(__name__)

    @app.route('/')
    def home():
        return "✅ Bot is alive!"

    def run():
        app.run(host="0.0.0.0", port=8080)

    thread = threading.Thread(target=run)
    thread.start()
