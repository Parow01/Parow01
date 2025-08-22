import logging
import os
from apscheduler.schedulers.background import BackgroundScheduler
from zoneinfo import ZoneInfo
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# 🔹 ENGINE IMPORTS
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
from alert_engine.alert_main import start_alert_engine

# ✅ Logging Setup
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

# ✅ Scheduler
scheduler = BackgroundScheduler(timezone=ZoneInfo("UTC"))

# ✅ Environment Variables
BOT_TOKEN = os.getenv("BOT_TOKEN")
RENDER_URL = os.getenv("RENDER_EXTERNAL_URL")  # Render provides this automatically

# ✅ Build Telegram App
app = ApplicationBuilder().token(BOT_TOKEN).build()

# ✅ Telegram Commands
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ UmarAlertBot is online via Webhook!")

app.add_handler(CommandHandler("start", start))

# ✅ Safe Engine Starter
def safe_start(module_name, func):
    try:
        func(scheduler)
        logging.info(f"✅ {module_name} started successfully.")
    except Exception as e:
        logging.error(f"❌ {module_name} failed: {e}")

# ✅ Start all modules
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
safe_start("Alert Engine", start_alert_engine)

# ✅ Start Scheduler
scheduler.start()

# ✅ Webhook Mode
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))  # Render sets PORT automatically
    logging.info(f"🌍 Starting webhook on port {port} at {RENDER_URL}")

    app.run_webhook(
        listen="0.0.0.0",
        port=port,
        url_path=BOT_TOKEN,
        webhook_url=f"{RENDER_URL}/{BOT_TOKEN}"
    )
