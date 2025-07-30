from apscheduler.schedulers.background import BackgroundScheduler
from whale_smartlist.smartlist_core import monitor_smartlist
from alert_manager.message_router import route_alert

def start_smartlist_monitor():
    scheduler = BackgroundScheduler()
    scheduler.add_job(run_smartlist_check, "interval", seconds=60)
    scheduler.start()

def run_smartlist_check():
    result = monitor_smartlist()
    if result:
        send_alert(result["alert"])
