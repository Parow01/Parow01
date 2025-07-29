# ✅ umaralertbot/liquidation_heatmap/heatmap_core.py

import os
import requests
import logging
from dotenv import load_dotenv

load_dotenv()

COINGLASS_API_KEY = os.getenv("COINGLASS_API_KEY")
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
        requests.post(url, data=payload)
        logging.info("✅ Liquidation alert sent.")
    except Exception as e:
        logging.error(f"❌ Failed to send liquidation alert: {e}")

def check_liquidation_clusters():
    try:
        url = "https://open-api.coinglass.com/public/v2/liquidation_chart"
        headers = {"coinglassSecret": COINGLASS_API_KEY}
        response = requests.get(url, headers=headers)
        data = response.json()

        if not data.get("success", False):
            logging.warning("❌ Coinglass API error")
            return

        clusters = []
        for item in data["data"]:
            symbol = item["symbol"]
            long_liq = item.get("longVolUsd", 0)
            short_liq = item.get("shortVolUsd", 0)
            total_liq = long_liq + short_liq

            if total_liq > 2_000_000:  # Cluster threshold
                clusters.append((symbol, long_liq, short_liq))

        if clusters:
            msg = "<b>🔥 Liquidation Heatmap Alert</b>\n\n"
            for sym, long_usd, short_usd in clusters:
                msg += f"<b>{sym}</b>:\n"
                msg += f"🟥 Longs: ${long_usd:,.0f}\n"
                msg += f"🟦 Shorts: ${short_usd:,.0f}\n\n"
            send_liquidation_alert(msg)

    except Exception as e:
        logging.error(f"❌ Error in heatmap engine: {e}")


