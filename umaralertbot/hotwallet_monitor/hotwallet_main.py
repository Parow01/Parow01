from apscheduler.schedulers.background import BackgroundScheduler
from hotwallet_monitor.hotwallet_core import check_hotwallet_activity

# Start hotwallet monitoring via scheduler (called from main.py)
def start_hotwallet_monitor(scheduler: BackgroundScheduler):
    scheduler.add_job(check_hotwallet_activity, 'interval', minutes=1, id='hotwallet_monitor', replace_existing=True)

# Called from alert engine (on-demand run)
def detect_hotwallet_movement():
    check_hotwallet_activity()








