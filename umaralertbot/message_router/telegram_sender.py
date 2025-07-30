import os
import requests

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")  # Optional: use dynamic IDs if needed

def send_telegram_alert(message: str, chat_id: str = None):
    if not BOT_TOKEN:
        raise Exception("❌ BOT_TOKEN is missing in environment variables.")
    
    chat_id = chat_id or CHAT_ID
    if not chat_id:
        raise Exception("❌ CHAT_ID is missing in environment variables.")

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "HTML"
    }
    
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
    except Exception as e:
        print(f"❌ Failed to send Telegram alert: {e}")
