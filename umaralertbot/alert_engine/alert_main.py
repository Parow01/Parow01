from apscheduler.schedulers.background import BackgroundScheduler
from alert_engine.alert_core import collect_all_alerts
from alert_manager.router_main import send_alert_to_telegram

def run_alert_engine(*args, **kwargs):
    """
    Runs the alert engine job.
    Accepts extra args/kwargs to avoid APScheduler errors.
    """
    print("[alert_engine] Running alert engine...")
    alerts = collect_all_alerts()
    for alert in alerts:
        send_alert_to_telegram(alert)
    print(f"[alert_engine] Sent {len(alerts)} alerts")

def start_alert_engine(scheduler: BackgroundScheduler):
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
