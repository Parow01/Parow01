# ✅ umaralertbot/hotwallet_monitor/hotwallet_main.py

from apscheduler.schedulers.background import BackgroundScheduler
from hotwallet_monitor.hotwallet_core import check_hotwallet_activity

def start_hotwallet_monitor():
    scheduler = BackgroundScheduler(timezone="Africa/Lagos")
    scheduler.add_job(check_hotwallet_activity, 'interval', minutes=6)
    scheduler.start()




