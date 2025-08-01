# ✅ umaralertbot/trading_strategy_engine/strategy_main.py

from apscheduler.schedulers.background import BackgroundScheduler
from trading_strategy_engine.strategy_core import generate_trading_signal
from alert_manager.alert_handler import send_alert_to_telegram
import logging

# 🔁 Scheduler-compatible engine runner
def start_strategy_engine(scheduler: BackgroundScheduler):
    def job():
        try:
            signal = generate_trading_signal()
            if signal:
                send_alert_to_telegram(signal)
        except Exception as e:
            logging.error(f"[Trading Strategy Engine Error] {e}")

    scheduler.add_job(job, trigger='interval', minutes=5, id='trading_engine_job', replace_existing=True)
    logging.info("✅ Trading Strategy engine job added to scheduler.")

# ✅ Confluence-compatible function for alert_engine
def detect_strategy_signal():
    try:
        signal = generate_trading_signal()
        if signal:
            return {
                "status": True,
                "message": signal.get("message", "📈 Trading Strategy Signal"),
                "confidence": signal.get("confidence", "medium")
            }
        return {"status": False}
    except Exception as e:
        logging.error(f"[Strategy Signal Detection Error] {e}")
        return {"status": False}


