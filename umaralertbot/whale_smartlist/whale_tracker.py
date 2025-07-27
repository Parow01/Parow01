import random

# Simulated Smartlist for now (can be upgraded with Arkham/Lookonchain scraping)
SMARTLIST = {
    "0xAlpha123": {"score": 0.78, "tag": "ETH Accumulator"},
    "0xWhale456": {"score": 0.81, "tag": "BTC Dip Buyer"},
    "0xQuiet789": {"score": 0.91, "tag": "Smart Layer 2 Player"}
}

def get_smart_whales():
    """Returns the current Smartlist of reliable whales"""
    return SMARTLIST

def detect_whale_activity() -> dict | None:
    """
    Simulate detection of a whale transaction from the Smartlist
    Later replaced with Arkham/Lookonchain hooks.
    """
    whale = random.choice(list(SMARTLIST.items()))
    address, info = whale

    if info["score"] >= 0.70:
        return {
            "type": "whale_tx",
            "address": address,
            "alert": f"🧠 Smart Whale ({info['tag']}) just made a move.\nConfidence: {int(info['score']*100)}%",
        }
    return None
