# ✅ umaralertbot/liquidation_heatmap/heatmap_core.py

import requests
import logging
import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")


def send_liquidation_alert(message: str):
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


def check_liquidation_clusters():
    """
    Core logic for detecting liquidation heatmap clusters across exchanges.
    This uses free Coinglass liquidation data.
    """
    try:
        logging.info("📊 Checking liquidation heatmap...")

        # Example free API from Coinglass (no key required)
        url = "https://open-api.coinglass.com/public/v2/liquidation_order"
        headers = {
            "accept": "application/json",
        }

        response = requests.get(url, headers=headers)
        data = response.json()

        # Real alert logic: cluster detection
        alerts = []

        for item in data.get("data", []):
            symbol = item.get("symbol")
            long_usd = item.get("longVolUsd", 0)
            short_usd = item.get("shortVolUsd", 0)

            total = long_usd + short_usd
            if total > 3_000_000:  # Customize this threshold in blueprint
                alert_msg = (
                    f"<b>🔥 Liquidation Cluster Alert</b>\n\n"
                    f"🪙 <b>Pair:</b> {symbol}\n"
                    f"💥 <b>Longs:</b> ${long_usd:,.0f}\n"
                    f"💣 <b>Shorts:</b> ${short_usd:,.0f}\n"
                    f"📊 <b>Total:</b> ${total:,.0f}\n\n"
                    f"<i>Large liquidation cluster detected. Possible reversal or breakout area.</i>"
                )
                alerts.append(alert_msg)

        for msg in alerts:
            send_liquidation_alert(msg)

    except Exception as e:
        logging.error(f"❌ Error while scanning liquidation heatmap: {e}")

