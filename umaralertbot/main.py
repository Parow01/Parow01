import os
import logging
from flask import Flask, request
import pytz
from apscheduler.schedulers.background import BackgroundScheduler

scheduler = BackgroundScheduler(timezone=pytz.utc)  # ⬅️ force pytz timezone
from dotenv import load_dotenv
import pytz

from keepalive import keep_alive
from message_router.router import process_update
# ✅ Engine Imports
from whale_engine.whale_main import start_whale_engine
from funding_rate_monitor.funding_main import start_funding_rate_monitor
from fomo_scanner.fomo_main import start_fomo_scanner
from liquidation_heatmap.heatmap_main import start_liquidation_heatmap
from confluence_engine.confluence_main import start_confluence_engine
from hotwallet_monitor.hotwallet_main import start_hotwallet_monitor
from exchange_reserve.reserve_main import start_reserve_monitor
from netflow_reaction.netflow_main import start_netflow_engine
from whale_sentiment.sentiment_main import start_sentiment_engine
from token_tracker.token_main import start_token_tracker
from trading_strategy_engine.strategy_main import start_trading_engine
from alert_engine.alert_main import start_alert_engine
from whale_smartlist.smartlist_main import start_smartlist_monitor

# ✅ Load environment variables
load_dotenv()

# ✅ Logging config
logging.basicConfig(level=logging.INFO)

# ✅ Telegram Bot Token
BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise Exception("❌ BOT_TOKEN is missing in the .env file")

# ✅ Set up Flask app
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

# ✅ Scheduler Setup
scheduler = BackgroundScheduler(timezone=pytz.UTC)
scheduler.start()

# ✅ Start All Engines Here (in background)
start_whale_engine(scheduler)
start_funding_rate_monitor(scheduler)
start_fomo_scanner(scheduler)
start_liquidation_heatmap(scheduler)
start_confluence_engine(scheduler)
start_hotwallet_monitor(scheduler)
start_reserve_monitor(scheduler)
start_netflow_engine(scheduler)
start_sentiment_engine(scheduler)
start_token_tracker(scheduler)
start_trading_engine(scheduler)
start_alert_engine(scheduler)
start_smartlist_monitor(scheduler)

# ✅ Keep app alive on Render
keep_alive(app)







