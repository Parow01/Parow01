import logging
import os
import requests
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def fetch_and_process_screener_data():
    try:
        logging.info("🔍 Whale Screener running...")

        # Example test alert
        alert_message = "🚨 [TEST] Whale Screener activated. Simulated whale detected."

        if BOT_TOKEN and CHAT_ID:
            url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
            data = {
                "chat_id": CHAT_ID,
                "text": alert_message,
                "parse_mode": "HTML"
            }
            response = requests.post(url, data=data)

            if response.status_code == 200:
                logging.info("✅ Whale Screener alert sent to Telegram.")
            else:
                logging.error(f"❌ Failed to send alert. Telegram response: {response.text}")
        else:
            logging.warning("⚠️ Missing TELEGRAM_BOT_TOKEN or TELEGRAM_CHAT_ID in .env")

    except Exception as e:
        logging.error(f"❌ Error in whale_screener core: {e}")

