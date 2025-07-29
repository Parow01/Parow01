# ✅ umaralertbot/funding_rate_monitor/funding_main.py

from apscheduler.schedulers.background import BackgroundScheduler
from funding_rate_monitor.funding_core import fetch_funding_data
import logging

def start_funding_monitor():
    try:
        scheduler = BackgroundScheduler(timezone="UTC")
        scheduler.add_job(fetch_funding_data, 'interval', minutes=7)
        scheduler.start()
        logging.info("✅ Funding Rate Monitor started.")
    except Exception as e:
        logging.error(f"❌ Error starting Funding Monitor: {e}")

