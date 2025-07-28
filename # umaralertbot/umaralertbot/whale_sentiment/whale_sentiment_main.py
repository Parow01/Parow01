# umaralertbot/whale_sentiment/whale_sentiment_main.py

import logging

logger = logging.getLogger(__name__)

def analyze_whale_sentiment(whale_data: list) -> str:
    """
    Analyze sentiment from whale activity.
    Example: If more inflows to exchanges → bearish, more outflows → bullish.
    """
    inflows = sum(1 for tx in whale_data if tx.get("type") == "inflow")
    outflows = sum(1 for tx in whale_data if tx.get("type") == "outflow")

    if inflows > outflows:
        sentiment = "Bearish whale sentiment detected (exchanges receiving more inflow)."
    elif outflows > inflows:
        sentiment = "Bullish whale sentiment detected (more outflows from exchanges)."
    else:
        sentiment = "Neutral whale sentiment."

    logger.info(f"Whale Sentiment Result: {sentiment}")
    return sentiment
