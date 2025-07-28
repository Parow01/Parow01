# screener_main.py

def start_whale_screener():
    print("✅ Whale Screener Engine is running...")
    # You can add your screener logic here

# umaralertbot/whale_screener/whale_screener_main.py

import logging

logger = logging.getLogger(__name__)

def screen_whale_transactions(transactions: list) -> list:
    """
    Screen whale transactions for unusual size or behavior.
    """
    threshold_usd = 1_000_000  # 1 million USD
    screened = []

    for tx in transactions:
        if tx.get("amount_usd", 0) >= threshold_usd:
            screened.append(tx)

    logger.info(f"Screened {len(screened)} whale transactions above ${threshold_usd}")
    return screened
