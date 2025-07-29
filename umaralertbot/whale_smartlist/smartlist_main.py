# ✅ umaralertbot/whale_smartlist/smartlist_main.py

import logging
from whale_smartlist.smartlist_core import detect_whale_activity
from alert_engine.alert_dispatcher import dispatch_alert

def run_smartlist_check():
    try:
        alert = detect_whale_activity()
        if alert:
            dispatch_alert(alert)
            logging.info("📡 [Smartlist Engine] Alert dispatched.")
        else:
            logging.info("✅ [Smartlist Engine] No smart whale activity detected.")
    except Exception as e:
        logging.error(f"❌ [Smartlist Engine Error] {e}")

def start_smartlist_engine(scheduler):
    try:
        scheduler.add_job(
            run_smartlist_check,
            trigger='interval',
            seconds=90,
            id='smartlist_engine_job',
            replace_existing=True
        )
        logging.info("✅ Smartlist engine scheduled successfully.")
    except Exception as e:
        logging.error(f"❌ Failed to start Smartlist Engine: {e}")
