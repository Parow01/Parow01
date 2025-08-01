# umaralertbot/hotwallet_monitor/hotwallet_main.py

from hotwallet_monitor.hotwallet_core import (
    fetch_etherscan_internal_txs,
    tag_known_wallets,
    detect_large_movements
)

def detect_hotwallet_movement():
    """
    Main entry point to run the hotwallet monitor pipeline.
    Returns a list of alert dictionaries if significant wallet activity is found.
    """
    alerts = []
    
    internal_txs = fetch_etherscan_internal_txs()
    if not internal_txs:
        return alerts

    tagged = tag_known_wallets(internal_txs)
    suspicious = detect_large_movements(tagged)

    for tx in suspicious:
        alerts.append({
            "type": "Hot Wallet Movement",
            "wallet": tx.get("wallet_tag", "Unknown"),
            "amount": tx["amount_usd"],
            "hash": tx["hash"],
            "timestamp": tx["timestamp"],
            "confidence": "high" if tx["amount_usd"] > 1_000_000 else "medium"
        })

    return alerts







