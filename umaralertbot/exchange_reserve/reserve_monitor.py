import random

def check_exchange_reserves() -> dict | None:
    """
    Simulates reserve movement signals.
    Replace with Arkham/Lookonchain data later.
    """
    btc_flow = random.choice(["inflow", "outflow"])
    usdt_change = random.choice(["increase", "decrease"])

    if btc_flow == "outflow" and usdt_change == "increase":
        return {
            "type": "reserves",
            "alert": "🏦 BTC Outflow + USDT Reserve Up → Possible Accumulation Detected!",
            "direction": "bullish"
        }

    elif btc_flow == "inflow" and usdt_change == "decrease":
        return {
            "type": "reserves",
            "alert": "🚨 BTC Inflow + USDT Draining → Possible Dump Setup!",
            "direction": "bearish"
        }

    return None
