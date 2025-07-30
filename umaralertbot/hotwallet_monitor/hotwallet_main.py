# ✅ umaralertbot/hotwallet_monitor/hotwallet_main.py

from apscheduler.schedulers.background import BackgroundScheduler
from hotwallet_monitor.hotwallet_core import detect_hotwallet_activity
from alert_engine.alert_manager import send_alert

def start_hotwallet_monitor():
    scheduler = BackgroundScheduler()
    scheduler.add_job(check_activity, "interval", seconds=120)
    scheduler.start()

def check_activity():
    result = detect_hotwallet_activity()
    if result:
        send_alert(result["alert"])


