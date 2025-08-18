from apscheduler.schedulers.background import BackgroundScheduler
from alert_engine.alert_core import collect_all_alerts
from alert_manager.router_main import send_alert_to_telegram
import pytz
import time

# Create scheduler with pytz to avoid zoneinfo error
scheduler = BackgroundScheduler(timezone=pytz.UTC)


def run_alert_engine(*args, **kwargs):
    """
    Runs the alert engine. Accepts extra args/kwargs
    to avoid APScheduler argument errors.
    """
    print("[alert_engine] Running alert engine...")
    alerts = collect_all_alerts()
    for alert in alerts:
        send_alert_to_telegram(alert)
    print(f"[alert_engine] Sent {len(alerts)} alerts")


def start_alert_engine():
    """
    Adds the alert engine job to the scheduler.
    """
    scheduler.add_job(
        run_alert_engine,
        "interval",
        seconds=60,
        id="alert_engine",
        replace_existing=True,
    )
    print("[alert_engine] Engine scheduled every 60 seconds")


if __name__ == "__main__":
    # Start the alert engine
    start_alert_engine()

    # Start scheduler
    scheduler.start()
    print("[main] Scheduler started successfully")

    # Keep the service alive
    try:
        while True:
            time.sleep(5)
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
        print("[main] Scheduler shut down")
