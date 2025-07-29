import logging
from whale_screener.screener_core import fetch_and_process_screener_data

def start_whale_screener(scheduler):
    try:
        scheduler.add_job(
            fetch_and_process_screener_data,
            trigger='interval',
            seconds=45,
            id='whale_screener_job',
            replace_existing=True
        )
        logging.info("✅ Whale Screener engine scheduled successfully.")
    except Exception as e:
        logging.error(f"❌ Failed to start whale_screener: {e}")

