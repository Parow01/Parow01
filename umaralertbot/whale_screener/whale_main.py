# ✅ umaralertbot/whale_screener/whale_main.py

from apscheduler.schedulers.background import BackgroundScheduler
from whale_screener.whale_core import fetch_and_process_whale_data
import logging

def start_whale_engine():
    """
    Initializes and starts the whale screener scheduler.
    """
    logging.info("🔁 Starting Whale Screener Engine...")

    scheduler = BackgroundScheduler()
    scheduler.add_job(fetch_and_process_whale_data, 'interval', minutes=5)
    scheduler.start()
   # whale_screener/whale_main.py

def start_whale_screener():
    from whale_screener.whale_core import run_screener
    run_screener()
 
