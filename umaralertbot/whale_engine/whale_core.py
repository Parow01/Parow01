# umaralertbot/whale_engine/whale_core.py

import requests

def fetch_whale_activity() -> dict | None:
    """
    Pull large wallet or tagged address activity from public APIs.
    Currently uses Whale Alert free endpoint with label filter logic.
    """
    try:
        url = "https://api.whale-alert.io/v1/transactions"
        params = {
            "api_key": "demo",  # Replace with real API key if needed
            "min_value": 1000000,
            "limit": 1
        }

        response = requests.get(url, params=params)
        data = response.json()

        if data.get("transactions"):
            tx = data["transactions"][0]
            label = tx.get("from", {}).get("owner_type", "unknown")
            symbol = tx.get("symbol", "crypto")
            amount = tx.get("amount", 0)
            to_label = tx.get("to", {}).get("owner_type", "unknown")

            alert = f"🐋 {amount} {symbol.upper()} moved from {label} to {to_label}"

            return {
                "type": "whale_transfer",
                "alert": alert,
                "confidence": "medium"
            }

    except Exception as e:
        print(f"[Whale Engine] Error: {e}")
    return None

