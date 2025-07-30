# umaralertbot/whale_engine/whale_main.py

from whale_engine.whale_core import fetch_whale_activity
from message_router.telegram_sender import send_telegram_alert

def run_whale_engine():
    alert = fetch_whale_activity()
    if alert:
        send_telegram_alert(alert["alert"])
