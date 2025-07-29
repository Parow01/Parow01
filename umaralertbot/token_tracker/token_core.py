# umaralertbot/token_tracker/token_core.py

import httpx

TOKEN_LIST = ["PEPE", "DOGE", "SHIB", "FLOKI", "WIF", "ORDI"]
SIGNAL_THRESHOLD = 2.5  # % price move within 15 min triggers alert

async def fetch_token_data():
    try:
        url = f"https://api.coingecko.com/api/v3/coins/markets"
        params = {
            "vs_currency": "usd",
            "ids": "",
            "order": "market_cap_desc",
            "per_page": 100,
            "page": 1,
            "sparkline": False,
            "price_change_percentage": "15m"
        }
        async with httpx.AsyncClient(timeout=10) as client:
            response = await client.get(url, params=params)
            response.raise_for_status()
            return response.json()
    except Exception as e:
        print(f"[token_tracker] Error fetching data: {e}")
        return []

async def track_tokens():
    data = await fetch_token_data()
    if not data:
        return None

    alerts = []

    for token in data:
        name = token.get("symbol", "").upper()
        if name in TOKEN_LIST:
            change_15m = token.get("price_change_percentage_15m_in_currency", 0)
            if change_15m is None:
                continue
            if abs(change_15m) >= SIGNAL_THRESHOLD:
                direction = "📈 Pumping" if change_15m > 0 else "📉 Dumping"
                alerts.append({
                    "type": "token_tracker",
                    "alert": f"{direction} Alert: {name} moved {round(change_15m, 2)}% in 15 min",
                    "confidence": "medium"
                })

    return alerts if alerts else None
