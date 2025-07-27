import random

# Simulated smartlist for now — later to be updated with Arkham or Whale Alert data
SMARTLIST = [
    {"address": "0xabc1", "confidence": 75, "behavior": "buys dips"},
    {"address": "0xabc2", "confidence": 68, "behavior": "sells rallies"},
    {"address": "0xabc3", "confidence": 82, "behavior": "accumulates bottoms"},
]

def get_reliable_whales() -> list:
    """
    Returns whales with ≥70% success rate.
    """
    return [w for w in SMARTLIST if w["confidence"] >= 70]

def simulate_whale_activity() -> dict | None:
    """
    Randomly simulates whether a top whale is active.
    """
    whale = random.choice(SMARTLIST)
    active = random.choice([True, False])

    if active and whale["confidence"] >= 70:
        return {
            "type": "whale",
            "address": whale["address"],
            "confidence": whale["confidence"],
            "behavior": whale["behavior"],
            "alert": f"🐳 Whale {whale['address']} active again! ({whale['confidence']}% success, {whale['behavior']})"
        }

    return None
