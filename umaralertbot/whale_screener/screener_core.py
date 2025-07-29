import logging
import os
import requests
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def send_telegram_alert(message):
    try:
        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
        payload = {
            "chat_id": CHAT_ID,
            "text": message,
            "parse_mode": "HTML"
        }
        response = requests.post(url, data=payload)
        response.raise_for_status()
        logging.info("✅ Whale Screener alert sent.")
    except Exception as e:
        logging.error(f"❌ Failed to send Whale Screener alert: {e}")

def fetch_and_process_screener_data():
    try:
        # Simulated screener logic (replace with real logic later)
        logging.info("🔍 Whale Screener running...")

        # Example mock result
        alert_msg = (
            "<b>🚨 Whale Screener Alert</b>\n\n"
            "Detected suspicious whale behavior on Binance:\n"
            "🪙 <b>Asset:</b> ETH\n"
            "💰 <b>Amount:</b> 8,000 ETH\n"
            "📦 <b>Type:</b> Wallet → Exchange\n"
            "⏰ <b>Time:</b> Now"
        )

        send_telegram_alert(alert_msg)

    except Exception as e:
        logging.error(f"❌ Error in whale_screener core: {e}")


