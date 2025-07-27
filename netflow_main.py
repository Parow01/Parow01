# umaralertbot/netflow_engine/netflow_main.py

from datetime import datetime
import random

def analyze_netflow(stablecoin_flow, price_change):
    """
    Determines signal based on netflow direction and price reaction.
    """
    signal = "neutral"

    if stablecoin_flow > 0:
        if price_change > 0:
            signal = "bullish"  # buying pressure confirmed
        elif price_change < 0:
            signal = "fakeout risk"  # inflow but price dumping
    elif stablecoin_flow < 0:
        if price_change < 0:
            signal = "bearish"
        elif price_change > 0:
            signal = "squeeze potential"  # outflow but price pumping

    return {
        "timestamp": str(datetime.utcnow()),
        "flow": stablecoin_flow,
        "price_change": price_change,
        "signal": signal
    }

# 🔄 Example netflow snapshot (replace with real data from scraper or webhook later)
def get_mock_netflow():
    return {
        "stablecoin_flow": round(random.uniform(-10000000, 10000000), 2),  # +/- 10M
        "price_change": round(random.uniform(-3, 3), 2)  # % change in 1h
    }
