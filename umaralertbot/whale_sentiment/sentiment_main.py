import time
from whale_sentiment.sentiment_core import get_whale_sentiment
from alert_manager.alert_dispatcher import send_telegram_alert

def start_whale_sentiment_monitor():
    while True:
        try:
            alert = get_whale_sentiment()
            if alert:
                send_telegram_alert(alert)
        except Exception as e:
            print(f"[Whale Sentiment Error] {e}")
        time.sleep(180)  # Adjust delay for API usage limits
