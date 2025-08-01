# ✅ umaralertbot/whale_sentiment/sentiment_main.py

from apscheduler.schedulers.background import BackgroundScheduler
from whale_sentiment.sentiment_core import fetch_whale_sentiment
from alert_manager.message_router import route_alert
import logging

# 🔁 Scheduler-compatible version for main.py
def start_sentiment_monitor(scheduler: BackgroundScheduler):  # ✅ renamed
    def job_sentiment_check():
        try:
            signal = fetch_whale_sentiment()
            if signal:
                route_alert(signal)
        except Exception as e:
            logging.error(f"[Whale Sentiment Job Error] {e}")

    scheduler.add_job(job_sentiment_check, 'interval', minutes=60)
    logging.info("✅ Whale Sentiment job added to scheduler.")

# ✅ Alert engine-compatible function
def detect_whale_sentiment():
    try:
        signal = fetch_whale_sentiment()
        if signal:
            return {
                "status": True,
                "message": signal.get("message", "🧠 Whale Sentiment Alert"),
                "confidence": signal.get("confidence", "medium")
            }
        else:
            return {"status": False}
    except Exception as e:
        logging.error(f"[Sentiment Engine] detect_whale_sentiment error: {e}")
        return {"status": False}




