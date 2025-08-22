from flask import Flask
import threading

def keep_alive():
    app = Flask("keepalive")

    @app.route("/")
    def home():
        return "✅ UmarAlertBot is alive and running on Render!"

    def run():
        # Run Flask on port 8080 for Render
        app.run(host="0.0.0.0", port=8080)

    # Start Flask in a background thread so it won't block your bot
    t = threading.Thread(target=run)
    t.daemon = True
    t.start()
