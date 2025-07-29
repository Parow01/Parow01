# ✅ umaralertbot/funding_rate_monitor/funding_core.py

import requests
import logging
import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def send_funding_alert(message):
    try:
        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
        payload = {
            "chat_id": CHAT_ID,
            "text": message,
            "parse_mode": "HTML"
        }
        response = requests.post(url, data=payload)
        response.raise_for_status()
        logging.info("✅ Funding alert sent.")
    except Exception as e:
        logging.error(f"❌ Failed to send funding alert: {e}")

def fetch_funding_data():
    """
    Fetches funding rates from Coinglass API for major pairs.
    Filters abnormal spikes and sends alert.
    """
    try:
        logging.info("🔍 Checking funding rates...")
        url = "https://open-api.coinglass.com/public/v2/funding"
        headers = {"coinglassSecret": "d47319d1-b2c2-4f60-b1cf-fda8d81fd772"}  # Public free tier

        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()

        if data["code"] != 200 or "data" not in data:
            raise ValueError("Unexpected response from Coinglass.")

        major_pairs = ["BTCUSDT", "ETHUSDT", "SOLUSDT", "LINKUSDT", "DOGEUSDT"]
        threshold = 0.05  # Alert if funding > 0.05% or < -0.05%

        alerts = []
        for coin_data in data["data"]:
            symbol = coin_data.get("symbol")
            if symbol not in major_pairs:
                continue

            avg_rate = float(coin_data.get("avgFundingRate", 0)) * 100  # Convert to %
            if abs(avg_rate) >= threshold:
                emoji = "📉" if avg_rate < 0 else "📈"
                alerts.append(f"{emoji} <b>{symbol}</b>: {avg_rate:.4f}% avg funding rate")

        if alerts:
            msg = "<b>🧠 Smart Funding Alert</b>\n\n" + "\n".join(alerts)
            send_funding_alert(msg)

    except Exception as e:
        logging.error(f"❌ Error fetching funding rates: {e}")
