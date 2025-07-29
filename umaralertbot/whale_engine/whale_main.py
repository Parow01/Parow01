# whale_main.py

import logging
from apscheduler.schedulers.background import BackgroundScheduler
from whale_engine.whale_core import fetch_and_process_whales
import pytz

def start_whale_engine(scheduler=None):
    try:
        if scheduler is None:
            scheduler = BackgroundScheduler(timezone=pytz.UTC)
            scheduler.start()
        
        scheduler.add_job(fetch_and_process_whales, 'interval', seconds=60)
        logging.info("✅ Whale engine scheduled successfully.")
    except Exception as e:
        logging.error(f"❌ Failed to schedule whale engine: {e}")
