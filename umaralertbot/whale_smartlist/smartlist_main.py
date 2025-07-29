# ✅ umaralertbot/whale_smartlist/smartlist_main.py

import logging
from whale_smartlist.smartlist_core import analyze_smart_wallet_activity
from whale_sentiment.sentiment_core import evaluate_whale_sentiment
from alert_engine.alert_dispatcher import dispatch_alert  # ✅ assumes your alert router exists

def run_smartlist_and_sentiment():
    try:
        smart_alert = analyze_smart_wallet_activity()
        sentiment_alert = evaluate_whale_sentiment()

        if smart_alert:
            dispatch_alert(smart_alert)

        if sentiment_alert:
            dispatch_alert(sentiment_alert)

        logging.info("🧠 [Smartlist + Sentiment] Run complete.")
    except Exception as e:
        logging.error(f"❌ [Smartlist Engine Error] {e}")

def start_smartlist_engine(scheduler):
    try:
        scheduler.add_job(
            run_smartlist_and_sentiment,
            trigger='interval',
            seconds=65,
            id='smartlist_engine_job',
            replace_existing=True
        )
        logging.info("✅ Smartlist + Sentiment Engine scheduled.")
    except Exception as e:
        logging.error(f"❌ Failed to start Smartlist engine: {e}")
