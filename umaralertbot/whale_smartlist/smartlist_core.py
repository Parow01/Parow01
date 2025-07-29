import random

WATCHLIST = {
    "SmartWhale01": "0xF977814e90dA44bFA03b6295A0616a897441aceC",
    "ArkhamWhale77": "0x742d35Cc6634C0532925a3b844Bc454e4438f44e"
}

def monitor_smartlist() -> dict | None:
    # Simulate some random "detected" events (replace with actual logic later)
    whale_name = random.choice(list(WATCHLIST.keys()))
    direction = random.choice(["deposit", "withdrawal"])
    amount = random.choice([500000, 1200000, 3000000])

    if amount >= 1000000:
        alert_msg = f"🐋 {whale_name} made a {direction.upper()} of ${amount:,}!"
        return {
            "type": "smartlist",
            "alert": alert_msg,
            "confidence": "high"
        }

    return None

