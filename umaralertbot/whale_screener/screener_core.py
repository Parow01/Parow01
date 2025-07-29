# ✅ umaralertbot/whale_screener/whale_core.py

import requests
import logging
import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def send_whale_alert(message):
    try:
        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
        payload = {
            "chat_id": CHAT_ID,
            "text": message,
            "parse_mode": "HTML"
        }
        response = requests.post(url, data=payload)
        response.raise_for_status()
        logging.info("✅ Whale alert sent.")
    except Exception as e:
        logging.error(f"❌ Failed to send whale alert: {e}")


def fetch_and_process_whale_data():
    """
    Blueprint Logic: Track wallet flows from tagged whales, institutions, or smart lists.
    """
    try:
        logging.info("🐋 Whale screener running...")

        # Simulated data — replace with real tagged wallet flows from Arkham/DEX Screener
        alert_msg = (
            "<b>🐋 Whale Screener Alert</b>\n\n"
            "💼 <b>Wallet:</b> 0xABC...123 (Smart Money)\n"
            "🪙 <b>Token:</b> $LINK\n"
            "📦 <b>Action:</b> Accumulated $980K on Binance\n"
            "⏱️ <b>Time:</b> Last 6 mins\n"
            "🔎 <i>Wallet flagged as Smart Money — Watch further behavior.</i>"
        )

        send_whale_alert(alert_msg)

    except Exception as e:
        logging.error(f"❌ Error in whale screener: {e}")


