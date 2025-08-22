
import requests
import logging
import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def send_whale_alert(message: str):
    """Send a whale alert to Telegram."""
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
    """Fetch whale activity (placeholder now)."""
    try:
        logging.info("🐋 Whale screener running...")

        # TODO: Replace with real whale wallet detection
        alert_msg = (
            "<b>🐋 Whale Screener Alert</b>\n\n"
            "💼 <b>Wallet:</b> 0xABC...123 (Smart Money)\n"
            "🪙 <b>Token:</b> $LINK\n"
            "📦 <b>Action:</b> Accumulated $980K on Binance\n"
            "⏱️ <b>Time:</b> Last 6 mins\n"
            "🔎 <i>Wallet flagged as Smart Money — Watch further behavior.</i>"
        )

        # Send Telegram alert
        send_whale_alert(alert_msg)

        return {
            "type": "whale_screener",
            "alert": alert_msg,
            "confidence": "low"
        }

    except Exception as e:
        logging.error(f"❌ Error in whale screener: {e}")
        return None

def detect_whale_activity():
    """Wrapper used by confluence_engine to check recent whale activity."""
    try:
        result = fetch_and_process_whale_data()
        if result:
            return {
                "status": True,
                "message": result["alert"],
                "confidence": result.get("confidence", "low")
            }
        else:
            return {"status": False}
    except Exception as e:
        logging.error(f"❌ detect_whale_activity failed: {e}")
        return {"status": False}

def run_screener():
    """Standalone runner for manual testing."""
    return fetch_and_process_whale_data()
     




