# ✅ umaralertbot/exchange_reserve/reserve_core.py

import requests
import logging
import os
from dotenv import load_dotenv
from alert_engine.send_alert import send_telegram_alert

load_dotenv()
COINGLASS_API_KEY = os.getenv("COINGLASS_API_KEY")

def analyze_exchange_reserves():
    """
    Tracks BTC and USDT reserves across major exchanges using Coinglass API.
    Triggers alerts if large movements occur.
    """
    try:
        logging.info("📦 Checking exchange reserves...")

        url = "https://api.coinglass.com/api/exchangeReserve"
        headers = {
            "accept": "application/json",
            "coinglassSecret": COINGLASS_API_KEY
        }

        response = requests.get(url, headers=headers, timeout=10)
        data = response.json()

        alerts = []
        if "data" in data:
            for reserve in data["data"]:
                exchange = reserve.get("exchangeName")
                btc_change = reserve.get("btcChange24h")
                usdt_change = reserve.get("usdtChange24h")

                if btc_change and abs(btc_change) > 1000:
                    alert = (
                        f"<b>📉 Exchange Reserve Alert</b>\n"
                        f"📦 <b>Exchange:</b> {exchange}\n"
                        f"💥 <b>BTC Change (24h):</b> {btc_change:.0f} BTC\n"
                        f"⚠️ <i>Significant BTC flow detected</i>"
                    )
                    alerts.append(alert)
                    send_telegram_alert(alert)

                if usdt_change and abs(usdt_change) > 50_000_000:
                    alert = (
                        f"<b>💰 Exchange Reserve Alert</b>\n"
                        f"📦 <b>Exchange:</b> {exchange}\n"
                        f"💥 <b>USDT Change (24h):</b> ${usdt_change:,.0f}\n"
                        f"⚠️ <i>Major stablecoin movement</i>"
                    )
                    alerts.append(alert)
                    send_telegram_alert(alert)

        # Determine signal direction based on total outflows/inflows (example logic)
        net_btc_outflow = sum(res.get("btcChange24h", 0) for res in data["data"])
        net_usdt_outflow = sum(res.get("usdtChange24h", 0) for res in data["data"])

        if net_btc_outflow < -10000 or net_usdt_outflow < -500_000_000:
            direction = "bullish"
        elif net_btc_outflow > 10000 or net_usdt_outflow > 500_000_000:
            direction = "bearish"
        else:
            direction = "neutral"

        return {
            "direction": direction,
            "alert": "\n\n".join(alerts) if alerts else "No major reserve changes."
        }

    except Exception as e:
        logging.error(f"❌ [ExchangeReserve] Error: {e}")
        return {
            "direction": "neutral",
            "alert": "❌ Error analyzing exchange reserves"
        }

