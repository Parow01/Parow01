# ✅ umaralertbot/fomo_scanner/fomo_core.py

import logging
import os
import requests
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def send_fomo_alert(message):
    try:
        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
        payload = {
            "chat_id": CHAT_ID,
            "text": message,
            "parse_mode": "HTML"
        }
        response = requests.post(url, data=payload)
        response.raise_for_status()
        logging.info("✅ FOMO alert sent.")
    except Exception as e:
        logging.error(f"❌ Failed to send FOMO alert: {e}")

def scan_fomo_trades():
    """
    Main FOMO scanning logic. Called by main.py
    """
    try:
        logging.info("🔍 FOMO Scanner running...")

        # Simulated FOMO alert — replace with real data logic later
        alert_msg = (
            "<b>🚨 FOMO Scanner Alert</b>\n\n"
            "Sudden buying activity detected:\n"
            "🪙 <b>Token:</b> PEPE\n"
            "📈 <b>Spike:</b> 12 wallets bought in 2 min\n"
            "🕵️ <b>New Wallets:</b> 87% are newly funded"
        )

        send_fomo_alert(alert_msg)

        # Return structure used by confluence or dispatchers
        return {
            "type": "fomo_scanner",
            "alert": "🚨 FOMO Spike: Token PEPE jumped 12% in 2 minutes!",
            "direction": "bullish"
        }

    except Exception as e:
        logging.error(f"❌ Error in FOMO scanner: {e}")
        return None



