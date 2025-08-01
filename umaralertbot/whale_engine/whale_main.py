# ✅ umaralertbot/whale_engine/whale_main.py

from apscheduler.schedulers.background import BackgroundScheduler
from whale_engine.whale_core import analyze_whale_data
from message_router.telegram_sender import send_telegram_alert
import logging

def whale_engine_job():
    try:
        result = analyze_whale_data()
        if result and result.get("alerts"):
            for alert in result["alerts"]:
                send_telegram_alert(alert)
    except Exception as e:
        logging.error(f"❌ Whale Engine Error: {e}")

def start_whale_engine(scheduler: BackgroundScheduler):
    scheduler.add_job(
        whale_engine_job,
        trigger='interval',
        minutes=5,
        id='whale_engine_job',
        replace_existing=True
    )

