# ✅ umaralertbot/funding_rate_monitor/funding_main.py

import logging
from funding_rate_monitor.funding_core import fetch_funding_rate_data, send_funding_rate_alert

def job_funding_monitor():
    logging.info("🔄 Checking funding rates...")
    alerts = fetch_funding_rate_data()
    send_funding_rate_alert(alerts)

# ✅ Called by main.py
def start_funding_rate_monitor(scheduler):
    scheduler.add_job(
        job_funding_monitor,
        trigger="interval",
        minutes=8,
        id="funding_rate_monitor",
        replace_existing=True
    )
    logging.info("✅ Funding rate monitor job added to scheduler.")

# ✅ Optional helper used by alert_engine (unchanged)
def check_funding_rate_skew():
    try:
        result = fetch_funding_rate_data()
        if result:
            return {
                "status": True,
                "message": result.get("alert"),
                "confidence": result.get("confidence", "medium")
            }
        else:
            return {"status": False}
    except Exception as e:
        logging.error(f"[Funding Rate Monitor Error] {e}")
        return {"status": False}


