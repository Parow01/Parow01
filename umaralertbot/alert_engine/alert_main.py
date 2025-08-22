import logging
from apscheduler.schedulers.background import BackgroundScheduler
from alert_engine.alert_core import collect_all_alerts
from alert_manager.router_main import send_alert_to_telegram
import os

ALERT_INTERVAL = int(os.getenv("ALERT_INTERVAL", 60))  # configurable interval

def run_alert_engine(*args, **kwargs):
    """
    Runs the alert engine job.
    Accepts extra args/kwargs to avoid APScheduler errors.
    """
    logging.info("[alert_engine] Running alert engine...")
    alerts = collect_all_alerts()

    sent_count = 0
    for alert in alerts:
        try:
            send_alert_to_telegram(alert)
            sent_count += 1
        except Exception as e:
            logging.error(f"[alert_engine] Failed to send alert: {e} | alert={alert}")

    if sent_count > 0:
        logging.info(f"[alert_engine] Sent {sent_count} alerts")
    else:
        logging.info("[alert_engine] No new alerts this cycle")

def start_alert_engine(scheduler: BackgroundScheduler):
    """
    Adds the alert engine job to the scheduler.
    """
    scheduler.add_job(
        run_alert_engine,
        "interval",
        seconds=ALERT_INTERVAL,
        id="alert_engine",
        replace_existing=True,
    )
    logging.info(f"[alert_engine] Engine scheduled every {ALERT_INTERVAL} seconds")
