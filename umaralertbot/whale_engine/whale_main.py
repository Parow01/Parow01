# 📄 umaralertbot/whale_engine/whale_main.py

from apscheduler.schedulers.background import BackgroundScheduler
from whale_engine.whale_core import analyze_whale_data
from message_router.telegram_sender import send_telegram_alert

def start_whale_engine(scheduler: BackgroundScheduler):
    scheduler.add_job(
        whale_engine_job,
        trigger='interval',
        minutes=5,
        id='whale_engine_job',
        replace_existing=True
    )

def whale_engine_job():
    try:
        result = analyze_whale_data()
        if result:
            send_telegram_alert(result)
    except Exception as e:
        print(f"❌ Whale Engine Error: {e}")

