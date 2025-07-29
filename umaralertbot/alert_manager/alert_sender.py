# alert_sender.py

import os
import requests
from alert_manager.alert_guard import is_duplicate
from alert_manager.alert_formatter import format_alert_message

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def send_to_telegram(alert: dict):
    """
    Sends the formatted alert to Telegram if it's not a duplicate.
    """
    if not TELEGRAM_TOKEN or not TELEGRAM_CHAT_ID:
        print("❌ Telegram credentials missing.")
        return

    message = format_alert_message(alert)
    if is_duplicate(message):
        print("⚠️ Duplicate alert skipped.")
        return

    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message,
        "parse_mode": "HTML",
        "disable_web_page_preview": True
    }

    try:
        response = requests.post(url, data=payload, timeout=10)
        response.raise_for_status()
        print("✅ Alert sent to Telegram.")
    except Exception as e:
        print(f"❌ Failed to send alert: {e}")
