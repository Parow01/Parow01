# smartlist_main.py

from apscheduler.schedulers.background import BackgroundScheduler
from whale_smartlist.smartlist_core import fetch_smart_whale_activity
from alert_manager.router_main import send_alert_to_telegram

def start_smartlist_engine(scheduler: BackgroundScheduler):
    scheduler.add_job(run_smartlist_engine, "interval", minutes=3, id="smartlist_engine", replace_existing=True)
    print("[whale_smartlist] Smartlist engine scheduled every 3 minutes")

def run_smartlist_engine():
    alerts = fetch_smart_whale_activity()
    for alert in alerts:
        send_alert_to_telegram(alert)

