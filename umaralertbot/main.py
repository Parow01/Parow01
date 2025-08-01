# ✅ umaralertbot/main.py

import logging
import os
import pytz
from keepalive import keep_alive
from apscheduler.schedulers.background import BackgroundScheduler
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# ✅ ENGINE IMPORTS
from whale_screener.whale_main import start_whale_screener
from fomo_scanner.fomo_main import start_fomo_scanner
from funding_rate_monitor.funding_main import start_funding_rate_monitor
from liquidation_heatmap.heatmap_main import start_liquidation_heatmap_monitor
from confluence_engine.confluence_main import start_confluence_engine
from netflow_reaction.netflow_main import start_netflow_monitor
from exchange_reserve.reserve_main import start_reserve_monitor
from hotwallet_monitor.hotwallet_main import start_hotwallet_monitor
from whale_sentiment.sentiment_main import start_sentiment_monitor
from whale_smartlist.smartlist_main import start_smartlist_monitor
from token_tracker.token_main import start_token_tracker
from trading_strategy_engine.strategy_main import start_strategy_engine
from alert_engine.alert_main import run_alert_engine

# ✅ Logging Setup
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

# ✅ Scheduler with pytz (to fix timezone error)
scheduler = BackgroundScheduler(timezone=pytz.utc)

# ✅ Telegram Setup
BOT_TOKEN = os.getenv("BOT_TOKEN")
app = ApplicationBuilder().token(BOT_TOKEN).build()

# ✅ Telegram Bot Command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ UmarAlertBot is online and running smoothly!")

app.add_handler(CommandHandler("start", start))

# ✅ Safe Engine Startup Wrapper
def safe_start(module_name, func):
    try:
        func(scheduler)  # Always pass scheduler to avoid argument mismatch
        logging.info(f"✅ {module_name} started successfully.")
    except Exception as e:
        logging.error(f"❌ {module_name} failed to start: {e}")

# ✅ START ALL MODULES
safe_start("Whale Screener", start_whale_screener)
safe_start("FOMO Scanner", start_fomo_scanner)
safe_start("Funding Rate Monitor", start_funding_rate_monitor)
safe_start("Liquidation Heatmap", start_liquidation_heatmap_monitor)
safe_start("Confluence Engine", start_confluence_engine)
safe_start("Netflow Monitor", start_netflow_monitor)
safe_start("Exchange Reserve Monitor", start_reserve_monitor)
safe_start("Hot Wallet Monitor", start_hotwallet_monitor)
safe_start("Whale Sentiment Monitor", start_sentiment_monitor)
safe_start("Whale Smartlist Monitor", start_smartlist_monitor)
safe_start("Token Tracker", start_token_tracker)
safe_start("Trading Strategy Engine", start_strategy_engine)
safe_start("Alert Engine", run_alert_engine)  # 🔔 Master router

# ✅ Start Everything
scheduler.start()
keep_alive()
app.run_polling()











