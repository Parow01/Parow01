# ✅ umaralertbot/funding_rate_monitor/funding_main.py

from apscheduler.schedulers.background import BackgroundScheduler
from funding_rate_monitor.funding_core import fetch_funding_rate_data, send_funding_rate_alert
import logging

def start_funding_rate_monitor():
    scheduler = BackgroundScheduler(timezone="UTC")
    scheduler.add_job(job_funding_monitor, "interval", minutes=8)
    scheduler.start()
    logging.info("✅ Funding rate monitor started.")

def job_funding_monitor():
    logging.info("🔄 Checking funding rates...")
    alerts = fetch_funding_rate_data()
    send_funding_rate_alert(alerts)

