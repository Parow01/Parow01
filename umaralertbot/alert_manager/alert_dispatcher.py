import os
import logging
import requests
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def send_telegram_alert(message, parse_mode="HTML"):
    """
    Send a formatted Telegram alert message to the configured chat.
    """
    try:
        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
        payload = {
            "chat_id": CHAT_ID,
            "text": message,
            "parse_mode": parse_mode
        }
        response = requests.post(url, data=payload)
        response.raise_for_status()
        logging.info("✅ Telegram alert sent successfully.")
    except Exception as e:
        logging.error(f"❌ Failed to send Telegram alert: {e}")
