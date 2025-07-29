# ✅ umaralertbot/fomo_scanner/fomo_main.py

from apscheduler.schedulers.background import BackgroundScheduler
from fomo_scanner.fomo_core import fetch_and_process_fomo_data

def start_fomo_scanner():
    scheduler = BackgroundScheduler()
    scheduler.add_job(fetch_and_process_fomo_data, 'interval', minutes=3)
    scheduler.start()


