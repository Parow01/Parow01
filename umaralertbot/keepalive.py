from flask import Flask
import threading

def keep_alive(app: Flask):
    def run():
        app.run(host="0.0.0.0", port=8080)

    t = threading.Thread(target=run)
    t.start()
