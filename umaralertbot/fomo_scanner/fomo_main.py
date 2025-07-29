# fomo_scanner/fomo_main.py

import logging
from apscheduler.schedulers.background import BackgroundScheduler
from fomo_scanner.fomo_core import fetch_fomo_signals

def start_fomo_scanner(scheduler: BackgroundScheduler):
    try:
        scheduler.add_job(fetch_fomo_signals, "interval", minutes=5, id="fomo_scanner_job", replace_existing=True)
        logging.info("✅ FOMO Scanner scheduled successfully.")
    except Exception as e:
        logging.error(f"❌ Failed to schedule FOMO Scanner: {e}")
