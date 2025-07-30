import requests
import logging

def analyze_whale_data():
    """
    Checks for significant whale transfers using Whale Alert API.
    Returns a structured alert dict if conditions are met.
    """
    try:
        url = "https://api.whale-alert.io/v1/transactions"
        params = {
            "api_key": "demo",  # Replace with your actual Whale Alert key if you upgrade
            "min_value": 1000000,
            "limit": 1
        }

        response = requests.get(url, params=params, timeout=10)
        data = response.json()

        if data.get("transactions"):
            tx = data["transactions"][0]
            symbol = tx.get("symbol", "crypto").upper()
            amount = tx.get("amount", 0)
            from_owner = tx.get("from", {}).get("owner_type", "unknown")
            to_owner = tx.get("to", {}).get("owner_type", "unknown")

            alert_msg = f"🐋 {amount} {symbol} transferred from {from_owner} to {to_owner}"

            return {
                "status": "ok",
                "alerts": [
                    {
                        "type": "whale_transfer",
                        "message": alert_msg,
                        "confidence": "medium"
                    }
                ]
            }

    except Exception as e:
        logging.error(f"[whale_core] Error fetching whale activity: {e}")

    return {
        "status": "ok",
        "alerts": []
    }

