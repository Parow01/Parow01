# ✅ umaralertbot/whale_sentiment/sentiment_core.py

def evaluate_whale_sentiment() -> dict | None:
    """
    Simulates sentiment analysis from whale wallet movements.
    """
    buy_count = 3
    sell_count = 1

    if buy_count > sell_count:
        return {
            "type": "sentiment",
            "alert": "🐋 Whale Sentiment: Accumulating aggressively",
            "confidence": "medium"
        }

    return None
