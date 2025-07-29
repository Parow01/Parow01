# strategy_core.py

import requests
from datetime import datetime, timedelta

COINGLASS_API_KEY = "YOUR_COINGLASS_API_KEY"  # Replace with your free API key
HEADERS = {"accept": "application/json", "coinglassSecret": COINGLASS_API_KEY}

def fetch_open_interest(symbol: str = "BTC") -> float | None:
    try:
        url = f"https://open-api.coinglass.com/public/v2/open_interest?symbol={symbol}&currency=USDT"
        response = requests.get(url, headers=HEADERS, timeout=10)
        data = response.json()

        if data["success"]:
            total_oi = data["data"]["totalOpenInterest"]
            return total_oi
    except Exception as e:
        print(f"[Strategy Engine] Error fetching OI: {e}")
    return None

def fetch_funding_rate(symbol: str = "BTC") -> float | None:
    try:
        url = f"https://open-api.coinglass.com/public/v2/funding_rate?symbol={symbol}"
        response = requests.get(url, headers=HEADERS, timeout=10)
        data = response.json()

        if data["success"]:
            avg_rate = float(data["data"]["binance"]["fundingRate"])
            return avg_rate
    except Exception as e:
        print(f"[Strategy Engine] Error fetching funding rate: {e}")
    return None

def generate_trading_signal() -> dict | None:
    oi = fetch_open_interest()
    fr = fetch_funding_rate()

    if oi is None or fr is None:
        return None

    if oi > 300000000 and fr > 0.01:
        return {
            "type": "strategy",
            "alert": "📈 Strategy Triggered: High OI + Positive Funding → Bullish Setup!",
            "confidence": "high"
        }
    elif oi > 300000000 and fr < -0.01:
        return {
            "type": "strategy",
            "alert": "📉 Strategy Triggered: High OI + Negative Funding → Bearish Setup!",
            "confidence": "high"
        }

    return None

