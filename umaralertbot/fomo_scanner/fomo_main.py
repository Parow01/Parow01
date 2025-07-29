# ✅ umaralertbot/fomo_scanner/fomo_main.py

from apscheduler.schedulers.background import BackgroundScheduler
from fomo_scanner.fomo_core import scan_fomo_trades
import logging

def start_fomo_scanner():
    scheduler = BackgroundScheduler()
    scheduler.add_job(scan_fomo_trades, 'interval', minutes=3)
    scheduler.start()
    logging.info("✅ FOMO Scanner scheduled to run every 3 minutes.")
