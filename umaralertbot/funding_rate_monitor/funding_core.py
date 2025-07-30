# ✅ umaralertbot/funding_rate_monitor/funding_core.py

import logging
import os
import requests
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def fetch_funding_rate_data():
    url = "https://fapi.coinglass.com/api/funding_rate?symbol=BTC"
    headers = {
        "accept": "application/json",
        "coinglassSecret": os.getenv("COINGLASS_API_KEY")
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        data = response.json()

        alerts = []
        for ex in data.get("data", []):
            rate = float(ex.get("fundingRate", 0))
            if abs(rate) >= 0.025:  # Threshold defined in blueprint
                direction = "🟢 Longs Overheating" if rate > 0 else "🔴 Shorts Overheating"
                alerts.append(f"{direction} — {ex['exchangeName']}: {rate:.4%}")

        return alerts

    except Exception as e:
        logging.error(f"❌ Error fetching funding rate data: {e}")
        return []

def send_funding_rate_alert(alerts):
    if not alerts:
        return

    message = "<b>⚠️ Funding Rate Alert</b>\n\n" + "\n".join(alerts)
    try:
        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
        payload = {
            "chat_id": CHAT_ID,
            "text": message,
            "parse_mode": "HTML"
        }
        response = requests.post(url, data=payload)
        response.raise_for_status()
        logging.info("✅ Funding rate alert sent.")
    except Exception as e:
        logging.error(f"❌ Failed to send funding rate alert: {e}")

# ✅ Used by confluence_engine
def analyze_funding_data():
    alerts = fetch_funding_rate_data()
    if alerts:
        return {
            "type": "funding_rate",
            "alert": "\n".join(alerts),
            "confidence": "medium"
        }
    return None

