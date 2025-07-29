# main.py

import os
import logging
from dotenv import load_dotenv
from flask import Flask, request
from keepalive import keep_alive
from apscheduler.schedulers.background import BackgroundScheduler
import pytz

from whale_engine.whale_main import start_whale_engine
# Add more imports here for other modules if needed

# Load environment variables
load_dotenv()

# Logging config
logging.basicConfig(level=logging.INFO)

# Telegram Bot Token
BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise Exception("❌ BOT_TOKEN is missing in the .env file")

# Set up Flask app
app = Flask(__name__)

@app.route('/')
def home():
    return "✅ UmarAlertBot is Running"

@app.route(f"/{BOT_TOKEN}", methods=["POST"])
def webhook():
    # Add your Telegram handler logic here
    return {"ok": True}

# Scheduler setup
scheduler = BackgroundScheduler(timezone=pytz.UTC)
scheduler.start()

# Start whale engine
start_whale_engine(scheduler)

# Keep app alive
keep_alive()




