import logging
import os
import requests
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def send_liquidation_alert(message):
    try:
        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
        payload = {
            "chat_id": CHAT_ID,
            "text": message,
            "parse_mode": "HTML"
        }
        response = requests.post(url, data=payload)
        response.raise_for_status()
        logging.info("✅ Liquidation alert sent.")
    except Exception as e:
        logging.error(f"❌ Failed to send liquidation alert: {e}")

def run_liquidation_job():
    try:
        logging.info("🧯 Liquidation Heatmap running...")

        # Mock logic: Replace with real data scraping/API
        alert_msg = (
            "<b>💥 Liquidation Alert</b>\n\n"
            "Massive longs liquidated on Bybit:\n"
            "📉 <b>Amount:</b> $38M\n"
            "📊 <b>Type:</b> Longs\n"
            "⏰ <b>Time:</b> Now"
        )

        send_liquidation_alert(alert_msg)

    except Exception as e:
        logging.error(f"❌ Error in liquidation heatmap: {e}")
        # ✅ umaralertbot/liquidation_heatmap/heatmap_core.py

def check_liquidation_clusters():
    """
    Simulated liquidation heatmap check. Replace with real implementation later.
    """
    return {
        "type": "liquidation_heatmap",
        "alert": "💥 Liquidation Cluster Detected near $28,500 BTC!",
        "level": "critical"
    }

