import logging
from apscheduler.schedulers.background import BackgroundScheduler
from whale_screener.whale_core import scan_whale_activity
from alert_engine.alert_dispatcher import dispatch_alert

def start_whale_engine(scheduler: BackgroundScheduler):
    scheduler.add_job(run_whale_engine, "interval", minutes=5)
    logging.info("🐋 Whale Screener Engine scheduled every 5 mins")

def run_whale_engine():
    try:
        logging.info("🔍 Whale Screener Engine triggered")
        alerts = scan_whale_activity()
        if alerts:
            for alert in alerts:
                dispatch_alert(alert)
    except Exception as e:
        logging.error(f"[whale_screener] Error: {e}")
