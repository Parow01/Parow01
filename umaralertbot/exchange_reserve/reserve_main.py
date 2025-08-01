# ✅ umaralertbot/exchange_reserve/reserve_main.py

from exchange_reserve.reserve_core import analyze_exchange_reserves
from alert_engine.send_alert import send_telegram_alert
import logging

def start_reserve_monitor(scheduler):
    def job_reserve_monitor():
        try:
            result = analyze_exchange_reserves()
            if result["direction"] != "neutral" and "No major" not in result["alert"]:
                message = f"<b>📦 Exchange Reserve Signal ({result['direction'].upper()})</b>\n\n{result['alert']}"
                send_telegram_alert(message)
        except Exception as e:
            logging.error(f"[Reserve Monitor] Job error: {e}")

    scheduler.add_job(job_reserve_monitor, 'interval', minutes=15, id="job_reserve_monitor", replace_existing=True)
    print("✅ Exchange reserve monitor job added to scheduler.")


def detect_reserve_shift():
    try:
        result = analyze_exchange_reserves()
        if result["direction"] != "neutral" and "No major" not in result["alert"]:
            message = f"<b>📦 Exchange Reserve Signal ({result['direction'].upper()})</b>\n\n{result['alert']}"
            send_telegram_alert(message)
    except Exception as e:
        logging.error(f"[Reserve Monitor] detect_reserve_shift() error: {e}")


