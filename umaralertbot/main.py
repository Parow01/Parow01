# ✅ umaralertbot/main.py

import asyncio
import logging
from pytz import UTC
from apscheduler.schedulers.background import BackgroundScheduler
from telegram import Bot
from telegram.ext import Application, CommandHandler

from keepalive import keep_alive
from whale_screener.whale_main import start_whale_engine
from fomo_scanner.fomo_main import start_fomo_scanner
from liquidation_heatmap.heatmap_main import start_liquidation_heatmap
from funding_rate_monitor.funding_main import start_funding_monitor
from confluence_engine.confluence_main import start_confluence_engine
from exchange_reserve.reserve_main import start_reserve_monitor
from hotwallet_monitor.hotwallet_main import start_hotwallet_monitor
from whale_sentiment.sentiment_main import start_sentiment_monitor
from whale_smartlist.smartlist_main import start_smartlist_monitor
from token_tracker.token_main import start_token_tracker
from trading_strategy_engine.strategy_main import start_strategy_engine
from alert_engine.alert_main import start_alert_engine
from dotenv import load_dotenv
import os

# ✅ Load environment variables
load_dotenv()
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

# ✅ Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# ✅ Telegram bot
bot = Bot(token=TELEGRAM_TOKEN)
application = Application.builder().token(TELEGRAM_TOKEN).build()

# ✅ Background scheduler with timezone
scheduler = BackgroundScheduler(timezone=UTC)

# ✅ Register background jobs from all modules
start_whale_engine(scheduler)
start_fomo_scanner(scheduler)
start_liquidation_heatmap(scheduler)
start_funding_monitor(scheduler)
start_confluence_engine(scheduler)
start_reserve_monitor(scheduler)
start_hotwallet_monitor(scheduler)
start_sentiment_monitor(scheduler)
start_smartlist_monitor(scheduler)
start_token_tracker(scheduler)
start_strategy_engine(scheduler)
start_alert_engine(scheduler)

# ✅ Flask server to keep Render instance alive
keep_alive()

# ✅ Start scheduler
scheduler.start()
print("✅ Scheduler started. All modules running.")

# ✅ Start Telegram bot loop
async def main():
    print("✅ Telegram bot starting...")
    await application.initialize()
    await application.start()
    await application.updater.start_polling()
    print("✅ Telegram bot running.")

asyncio.run(main())








