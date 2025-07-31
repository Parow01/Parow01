# smartlist_main.py

from apscheduler.schedulers.background import BackgroundScheduler
from whale_smartlist.smartlist_core import fetch_smart_whale_activity
from alert_manager.alert_handler import send_alert_to_telegram

def start_smartlist_monitor(scheduler: BackgroundScheduler):
    def job():
        alerts = fetch_smart_whale_activity()
        for alert in alerts:
            send_alert_to_telegram(alert)

    scheduler.add_job(job, trigger='interval', minutes=5, id='smartlist_monitor_job', replace_existing=True)


