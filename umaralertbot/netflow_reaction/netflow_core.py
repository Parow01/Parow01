# ✅ umaralertbot/netflow_reaction/netflow_core.py

import requests
import logging
import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def fetch_netflow_data():
    """
    Fetch recent exchange netflow data from CryptoQuant free API.
    This demo logic assumes outflows > inflows = bullish.
    """
    try:
        response = requests.get("https://api.cryptoquant.com/v1/btc/exchange-flows", timeout=10)
        data = response.json()

        netflow = float(data["data"]["netflow_1h"])
        price_change = float(data["data"]["price_change_15m"])

        if abs(netflow) < 100:
            return None  # ignore weak flow

        direction = "📉 Bearish" if netflow > 0 and price_change < 0 else "📈 Bullish"

        alert_msg = (
            f"<b>💸 Netflow Reaction Alert</b>\n\n"
            f"🔄 <b>Netflow:</b> {netflow:.2f} BTC\n"
            f"📊 <b>Price 15m:</b> {price_change:.2f}%\n"
            f"🧠 <b>Market Reaction:</b> {direction}"
        )

        return alert_msg

    except Exception as e:
        logging.error(f"❌ Netflow fetch error: {e}")
        return None


def send_netflow_alert(message):
    try:
        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
        payload = {
            "chat_id": CHAT_ID,
            "text": message,
            "parse_mode": "HTML"
        }
        requests.post(url, data=payload)
        logging.info("✅ Netflow alert sent.")
    except Exception as e:
        logging.error(f"❌ Failed to send netflow alert: {e}")

