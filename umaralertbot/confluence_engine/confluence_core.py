import logging
import os
import requests
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def send_telegram_alert(message):
    try:
        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
        payload = {
            "chat_id": CHAT_ID,
            "text": message,
            "parse_mode": "HTML"
        }
        response = requests.post(url, data=payload)
        response.raise_for_status()
        logging.info("✅ Confluence alert sent.")
    except Exception as e:
        logging.error(f"❌ Failed to send Confluence alert: {e}")

def run_confluence_engine():
    try:
        logging.info("🔄 Confluence Engine running...")

        # Simulated signals from other engines
        whale_activity = True
        liquidation_cluster = True
        fomo_volume_spike = False

        if whale_activity and liquidation_cluster:
            message = (
                "<b>📊 Confluence Signal Detected</b>\n\n"
                "✅ Whale Transfer Detected\n"
                "💥 Liquidation Cluster Confirmed\n"
                "📉 Market Reaction Likely\n\n"
                "This is a smart money trigger. Monitor closely. ⚠️"
            )
            send_telegram_alert(message)

    except Exception as e:
        logging.error(f"❌ Error in Confluence Engine: {e}")
