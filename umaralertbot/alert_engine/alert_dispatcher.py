# umaralertbot/alert_engine/alert_dispatcher.py

import os
import logging
import requests
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def dispatch_alert(message: str):
    """Send alert to Telegram"""
    try:
        if not TELEGRAM_TOKEN or not CHAT_ID:
            raise ValueError("Missing TELEGRAM_TOKEN or CHAT_ID in .env")

        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
        payload = {"chat_id": CHAT_ID, "text": message, "parse_mode": "HTML"}

        response = requests.post(url, data=payload)
        response.raise_for_status()

        logging.info(f"[ALERT] Sent: {message[:100]}")

    except Exception as e:
        logging.error(f"[ALERT ERROR] {e}")
