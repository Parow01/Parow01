# ✅ umaralertbot/whale_screener/whale_main.py

import logging
from apscheduler.schedulers.background import BackgroundScheduler
from whale_screener.whale_core import fetch_whale_alert
from alert_engine.alert_dispatcher import dispatch_alert

def start_whale_engine(scheduler: BackgroundScheduler):
    """
    Schedules the Whale Screener to run every 5 minutes.
    """
    scheduler.add_job(run_whale_screener, 'interval', minutes=5)
    logging.info("✅ Whale Screener scheduled every 5 minutes")

def run_whale_screener():
    try:
        signal = fetch_whale_alert()
        if signal:
            dispatch_alert(signal)
    except Exception as e:
        logging.error(f"[whale_screener] Error running screener: {e}")
