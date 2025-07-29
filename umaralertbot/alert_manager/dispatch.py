# ✅ umaralertbot/alert_manager/dispatch.py

import os
import requests
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")  # default Telegram alert chat

def send_alert(message: str, chat_id: str = None) -> None:
    """
    Sends a message to the specified Telegram chat.
    If no chat_id is provided, uses default CHAT_ID.
    """
    if not BOT_TOKEN:
        raise ValueError("❌ BOT_TOKEN missing in environment")

    if not chat_id:
        chat_id = CHAT_ID

    if not chat_id:
        raise ValueError("❌ CHAT_ID missing in environment or call")

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "HTML"
    }

    try:
        response = requests.post(url, data=payload, timeout=10)
        response.raise_for_status()
    except Exception as e:
        print(f"[ALERT DISPATCH ERROR] {e}")
