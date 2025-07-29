# ✅ umaralertbot/funding_rate_monitor/funding_main.py

import logging
from funding_rate_monitor.funding_rate_monitor_main import monitor_funding_rates

def run_funding_rate_check():
    try:
        monitor_funding_rates()
        logging.info("📡 [Funding Rate Monitor] Check complete.")
    except Exception as e:
        logging.error(f"❌ [Funding Rate Monitor Error] {e}")

def start_funding_rate_monitor(scheduler):
    try:
        scheduler.add_job(
            run_funding_rate_check,
            trigger='interval',
            seconds=120,
            id='funding_rate_monitor_job',
            replace_existing=True
        )
        logging.info("✅ Funding Rate Monitor scheduled successfully.")
    except Exception as e:
        logging.error(f"❌ Failed to start Funding Rate Monitor: {e}")

