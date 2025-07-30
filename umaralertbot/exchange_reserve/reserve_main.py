# ✅ umaralertbot/exchange_reserve/reserve_main.py

from apscheduler.schedulers.background import BackgroundScheduler
from exchange_reserve.reserve_core import analyze_exchange_reserves
from alert_engine.send_alert import send_telegram_alert
import logging

def start_reserve_monitor():
    scheduler = BackgroundScheduler()

    def job():
        try:
            result = analyze_exchange_reserves()
            if result["direction"] != "neutral" and "No major" not in result["alert"]:
                message = f"<b>📦 Exchange Reserve Signal ({result['direction'].upper()})</b>\n\n{result['alert']}"
                send_telegram_alert(message)
        except Exception as e:
            logging.error(f"[Reserve Monitor] Job error: {e}")

    scheduler.add_job(job, 'interval', minutes=15)
    scheduler.start()

