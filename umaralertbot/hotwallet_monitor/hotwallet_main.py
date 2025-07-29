# ✅ umaralertbot/hotwallet_monitor/hotwallet_main.py

import logging
from hotwallet_monitor.hotwallet_core import check_exchange_wallet_flows
from alert_engine.alert_manager import send_alert

def run_hotwallet_check():
    try:
        signal = check_exchange_wallet_flows()
        if signal:
            send_alert(signal["alert"])
        logging.info("♨️ [Hot Wallet Monitor] Check complete.")
    except Exception as e:
        logging.error(f"❌ [Hot Wallet Monitor Error] {e}")

def start_hotwallet_monitor(scheduler):
    try:
        scheduler.add_job(
            run_hotwallet_check,
            trigger='interval',
            seconds=90,
            id='hotwallet_monitor_job',
            replace_existing=True
        )
        logging.info("✅ Hot Wallet Monitor scheduled successfully.")
    except Exception as e:
        logging.error(f"❌ Failed to schedule Hot Wallet Monitor: {e}")
