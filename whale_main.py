# umaralertbot/whale_tracker/whale_main.py

import json
from datetime import datetime

# Dummy whale list for now (we'll later integrate Arkham/Whale Alert scraping)
SMARTLIST = {}

CONFIDENCE_THRESHOLD = 0.70

def tag_whale(address, tx_history):
    """
    Assigns a whale confidence score based on how often their actions precede major moves.
    """
    success_rate = calculate_success_rate(tx_history)
    if success_rate >= CONFIDENCE_THRESHOLD:
        SMARTLIST[address] = {
            'score': round(success_rate, 2),
            'last_seen': str(datetime.utcnow()),
            'tx_count': len(tx_history)
        }

def calculate_success_rate(tx_history):
    """
    Dummy scoring: % of transactions that caused +2% or -2% price move within 2h.
    """
    if not tx_history:
        return 0.0
    success_count = sum(1 for tx in tx_history if abs(tx['price_move']) >= 2)
    return success_count / len(tx_history)

def get_smartlist():
    return SMARTLIST

def load_whale_data(json_path="umaralertbot/data/whale_activity.json"):
    try:
        with open(json_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_smartlist(path="umaralertbot/data/smartlist.json"):
    with open(path, 'w') as file:
        json.dump(SMARTLIST, file, indent=2)
