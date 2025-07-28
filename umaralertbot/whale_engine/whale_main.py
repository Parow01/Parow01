scheduler.add_job(send_whale_alert, "interval", minutes=10, timezone=pytz.utc)

# whale_engine/whale_main.py

import requests
import logging
from apscheduler.schedulers.background import BackgroundScheduler
from telegram import Bot

# Your Telegram bot token and chat ID
BOT_TOKEN = "8092340392:AAHJN8d8mjQgHQeSAEyIYjEu0PesfQf0GH4"
CHAT_ID = "-1002078661647"

bot = Bot(token=BOT_TOKEN)

def send_whale_alert():
    try:
        # Simulated data (replace this with real API call if needed)
        alert_data = {
            "symbol": "ETH",
            "amount": "4,000 ETH",
            "exchange": "Binance",
            "direction": "Deposit"
        }

        message = (
            f"🟡 Whale Alert Detected!\n\n"
            f"Token: {alert_data['symbol']}\n"
            f"Amount: {alert_data['amount']}\n"
            f"Exchange: {alert_data['exchange']}\n"
            f"Direction: {alert_data['direction']}"
        )

        bot.send_message(chat_id=CHAT_ID, text=message)

    except Exception as e:
        logging.error(f"[Whale Alert] Failed to send alert: {e}")

def start_whale_engine():
    scheduler = BackgroundScheduler()
    scheduler.add_job(send_whale_alert, "interval", minutes=10)
    scheduler.start()
    logging.info("[Whale Engine] Running every 10 minutes.")
