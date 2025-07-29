# ✅ umaralertbot/netflow_reaction/netflow_main.py

from apscheduler.schedulers.background import BackgroundScheduler
from netflow_reaction.netflow_core import fetch_netflow_data, send_netflow_alert
import logging

def start_netflow_engine():
    scheduler = BackgroundScheduler()
    scheduler.add_job(check_netflow_event, 'interval', minutes=5)
    scheduler.start()
    logging.info("🚀 Netflow Engine started.")

def check_netflow_event():
    alert = fetch_netflow_data()
    if alert:
        send_netflow_alert(alert)

