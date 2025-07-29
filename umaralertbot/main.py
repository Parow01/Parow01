import os
import logging
from flask import Flask, request
from apscheduler.schedulers.background import BackgroundScheduler
from dotenv import load_dotenv
import pytz

from keepalive import keep_alive
from message_router.router import process_update

# Engine Imports ✅
from whale_engine.whale_main import start_whale_engine
from fomo_scanner.fomo_main import start_fomo_scanner
from whale_screener.screener_main import start_whale_screener
from liquidation_heatmap.heatmap_main import start_liquidation_heatmap
from funding_rate_monitor.funding_main import start_funding_rate_monitor
from confluence_engine.confluence_main import start_confluence_engine
# Add more here as you build them

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
    try:
        update = request.get_json()
        process_update(update)
    except Exception as e:
        logging.error(f"❌ Error in webhook: {e}")
    return {"ok": True}

# Scheduler setup
scheduler = BackgroundScheduler(timezone=pytz.UTC)
scheduler.start()

# 🔁 Start All Engines Here
start_whale_engine(scheduler)
start_fomo_scanner(scheduler)
start_whale_screener(scheduler)
start_liquidation_heatmap(scheduler)
start_funding_rate_monitor(scheduler)
start_confluence_engine(scheduler)
# Add more as needed

# Keep app alive
keep_alive(app)






