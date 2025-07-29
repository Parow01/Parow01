# ✅ umaralertbot/whale_screener/whale_main.py

from apscheduler.schedulers.background import BackgroundScheduler
from whale_screener.whale_core import fetch_and_process_whale_data

def start_whale_screener():
    scheduler = BackgroundScheduler()
    scheduler.add_job(fetch_and_process_whale_data, 'interval', minutes=4)
    scheduler.start()


