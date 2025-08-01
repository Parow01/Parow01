# ✅ umaralertbot/netflow_reaction/netflow_main.py

from apscheduler.schedulers.background import BackgroundScheduler
from netflow_reaction.netflow_core import fetch_netflow_data, send_netflow_alert
import logging

# ✅ Background job for main.py
def start_netflow_monitor(scheduler: BackgroundScheduler):
    def check_netflow_event():
        try:
            alert = fetch_netflow_data()
            if alert:
                send_netflow_alert(alert)
        except Exception as e:
            logging.error(f"[Netflow Monitor] Error: {e}")

    scheduler.add_job(check_netflow_event, 'interval', minutes=5)
    logging.info("✅ Netflow monitor job added to scheduler.")

# ✅ Alert engine-compatible function
def detect_netflow_reaction():
    try:
        alert = fetch_netflow_data()
        if alert:
            return {
                "status": True,
                "message": alert.get("message", "🚨 Netflow Alert"),
                "confidence": alert.get("confidence", "medium")
            }
        else:
            return {"status": False}
    except Exception as e:
        logging.error(f"[Netflow Reaction Error] {e}")
        return {"status": False}

