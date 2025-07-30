import time
import logging
from whale_sentiment.sentiment_core import fetch_whale_sentiment
from alert_manager.message_router import route_alert

def start_sentiment_engine():
    """
    Starts the whale sentiment monitoring engine.
    Called from main.py and runs in background.
    """
    while True:
        logging.info("🔁 Whale Sentiment Engine cycle started...")
        signal = fetch_whale_sentiment()
        if signal:
            route_alert(signal)
        time.sleep(3600)  # Runs every hour

