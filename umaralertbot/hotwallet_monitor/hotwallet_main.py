# ✅ umaralertbot/hotwallet_monitor/hotwallet_main.py

from apscheduler.schedulers.background import BackgroundScheduler
from hotwallet_monitor.hotwallet_core import check_hotwallet_activity

def start_hotwallet_monitor():
    scheduler = BackgroundScheduler(timezone="Africa/Lagos")
    scheduler.add_job(check_hotwallet_activity, 'interval', minutes=6)
    scheduler.start()
    # ✅ Add this at the bottom of hotwallet_main.py

from hotwallet_monitor.hotwallet_core import analyze_hotwallet_activity
from alert_engine.send_alert import send_telegram_alert
import logging

def detect_hotwallet_movement():
    try:
        alerts = analyze_hotwallet_activity()
        for message in alerts:
            send_telegram_alert(f"<b>🚨 Hot Wallet Movement</b>\n\n{message}")
    except Exception as e:
        logging.error(f"[Hotwallet Monitor] detect_hotwallet_movement() error: {e}")





