from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
from datetime import datetime
import pytz
import time

def send_whale_alert():
    print("🐋 Sending whale alert...")

def start_whale_engine(scheduler):
    scheduler.add_job(fetch_and_process_whales, 'interval', seconds=60)

    scheduler = BackgroundScheduler(timezone=pytz.utc)

    scheduler.add_job(
        send_whale_alert,
        trigger=IntervalTrigger(minutes=10),
        next_run_time=datetime.now(pytz.utc),
        id='whale_alert_job',
        replace_existing=True
    )

    scheduler.start()
    print("✅ Whale Engine scheduler started.")

    try:
        while True:
            time.sleep(60)
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
        print("❌ Whale Engine stopped.")

