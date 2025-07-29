import logging
from fomo_scanner.fomo_core import fetch_and_process_fomo_data

def start_fomo_scanner(scheduler):
    try:
        scheduler.add_job(
            fetch_and_process_fomo_data,
            trigger='interval',
            seconds=60,
            id='fomo_scanner_job',
            replace_existing=True
        )
        logging.info("✅ FOMO Scanner engine scheduled successfully.")
    except Exception as e:
        logging.error(f"❌ Failed to start fomo_scanner: {e}")
