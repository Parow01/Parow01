import os
import requests
import logging

BOT_TOKEN = os.getenv("BOT_TOKEN")
API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"

def send_message(chat_id, text):
    try:
        url = f"{API_URL}/sendMessage"
        payload = {"chat_id": chat_id, "text": text}
        response = requests.post(url, json=payload)
        response.raise_for_status()
        logging.info(f"✅ Message sent to {chat_id}")
    except Exception as e:
        logging.error(f"❌ Failed to send message: {e}")

def process_update(update):
    try:
        message = update.get("message")
        if not message:
            return

        chat_id = message["chat"]["id"]
        text = message.get("text", "")

        if text == "/start":
            send_message(chat_id, "👋 Welcome to UmarAlertBot!\n\nYou’ll receive real-time whale alerts and alpha signals here.")
        elif text == "/help":
            send_message(chat_id, "📘 *Commands:*\n/start – Welcome message\n/help – Show this help menu")
        else:
            send_message(chat_id, "❓ Unrecognized command. Try /help")
    except Exception as e:
        logging.error(f"❌ Error in process_update: {e}")
