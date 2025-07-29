# ✅ umaralertbot/netflow_engine/netflow_core.py

import logging
import random
import os
import requests
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def send_netflow_alert(message):
    try:
        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
        payload = {
            "chat_id": CHAT_ID,
            "text": message,
            "parse_mode": "HTML"
        }
        response = requests.post(url, data=payload)
        response.raise_for_status()
        logging.info("✅ Netflow alert sent.")
    except Exception as e:
        logging.error(f"❌ Failed to send Netflow alert: {e}")

def simulate_netflow_data():
    # Simulated dummy values (replace later with real Glassnode/API-free logic)
    inflow = random.randint(500, 5000)
    outflow = random.randint(500, 5000)
    price_movement = random.uniform(-2, 2)  # % price change in 15m

    return {
        "inflow": inflow,
        "outflow": outflow,
        "price_change": price_movement
    }

def run_netflow_engine():
    try:
        logging.info("📡 Netflow engine running...")

        data = simulate_netflow_data()
        inflow = data["inflow"]
        outflow = data["outflow"]
        price_change = data["price_change"]

        if inflow > 3000 and price_change < -1.5:
            alert = (
                "<b>🚨 Netflow Alert: Bearish Signal</b>\n\n"
                f"📥 Exchange Inflow: {inflow} BTC\n"
                f"📉 Price Dropped: {price_change:.2f}%\n\n"
                "→ Possible sell pressure or panic exit. Monitor."
            )
            send_netflow_alert(alert)

        elif outflow > 3000 and price_change > 1.5:
            alert = (
                "<b>🚀 Netflow Alert: Bullish Signal</b>\n\n"
                f"📤 Exchange Outflow: {outflow} BTC\n"
                f"📈 Price Increased: +{price_change:.2f}%\n\n"
                "→ Smart money accumulation likely."
            )
            send_netflow_alert(alert)

    except Exception as e:
        logging.error(f"❌ Error in Netflow Engine: {e}")
