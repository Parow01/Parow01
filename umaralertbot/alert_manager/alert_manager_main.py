# umaralertbot/alert_manager/alert_manager_main.py

import logging
import requests
from config import TELEGRAM_BOT_TOKEN

logger = logging.getLogger(__name__)

def send_telegram_alert(chat_id, message):
    """
    Sends alert to Telegram user.
    """
    try:
        url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
        payload = {
            "chat_id": chat_id,
            "text": message,
            "parse_mode": "Markdown"
        }
        response = requests.post(url, json=payload)
        response.raise_for_status()
        logger.info(f"Alert sent to {chat_id}: {message}")
        return response.json()

    except Exception as e:
        logger.error(f"Failed to send alert: {e}")
        return None
