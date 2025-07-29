import requests
from alert_engine.send_alert import send_telegram_alert

def check_exchange_reserves():
    try:
        url = "https://api.coinglass.com/api/exchangeReserve"
        headers = {
            "accept": "application/json",
            "coinglassSecret": "your_coinglass_api_key_here"
        }

        response = requests.get(url, headers=headers, timeout=10)
        data = response.json()

        if "data" in data:
            for reserve in data["data"]:
                exchange = reserve.get("exchangeName")
                btc_change = reserve.get("btcChange24h")
                usdt_change = reserve.get("usdtChange24h")

                if btc_change and abs(btc_change) > 1000:
                    alert = f"📉 Exchange Reserve Alert: {exchange} BTC reserves changed by {btc_change:.0f} BTC in 24h."
                    send_telegram_alert(alert)

                if usdt_change and abs(usdt_change) > 50_000_000:
                    alert = f"💰 Exchange Reserve Alert: {exchange} USDT reserves changed by ${usdt_change:,.0f} in 24h."
                    send_telegram_alert(alert)

    except Exception as e:
        print(f"[ExchangeReserve] Error: {e}")
