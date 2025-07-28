def start_whale_engine():
    ...
    
# umaralertbot/whale_engine/whale_main.py

from datetime import datetime
import random

# Mock whale data
MOCK_WHALES = [
    {"address": "0xabc1", "tx_history": [5.2, -1.1, 3.9]},
    {"address": "0xdef2", "tx_history": [1.0, -0.5, -2.2]},
    {"address": "0xghi3", "tx_history": [6.0, 5.1, 4.3]},
]

def calculate_confidence_score(tx_history):
    """
    Scores whale based on positive performance (% moves after tx).
    """
    profitable_trades = [p for p in tx_history if p > 0]
    if not tx_history:
        return 0
    return round(len(profitable_trades) / len(tx_history) * 100, 2)

def build_smartlist():
    """
    Filters whales with ≥70% accuracy and repeated behavior.
    """
    smartlist = []
    for whale in MOCK_WHALES:
        score = calculate_confidence_score(whale["tx_history"])
        if score >= 70 and len(whale["tx_history"]) >= 3:
            smartlist.append({
                "address": whale["address"],
                "score": score,
                "last_seen": str(datetime.utcnow())
            })
    return smartlist
