# ✅ umaralertbot/fomo_scanner/fomo_main.py

import logging
from fomo_scanner.fomo_core import fetch_and_process_fomo_data

def job_fomo_scan():
    logging.info("🔄 Scanning for FOMO tokens...")
    fetch_and_process_fomo_data()

def start_fomo_scanner(scheduler):  # ✅ Accept centralized scheduler
    scheduler.add_job(
        job_fomo_scan,
        trigger="interval",
        minutes=4,
        id="fomo_scanner_job",
        replace_existing=True
    )
    logging.info("✅ FOMO scanner job added to scheduler.")

def check_fomo_signals():
    try:
        result = fetch_and_process_fomo_data()
        if result:
            return {
                "status": True,
                "message": result["alert"],
                "confidence": "medium"
            }
        else:
            return {"status": False}
    except Exception as e:
        logging.error(f"[FOMO Scanner Error] {e}")
        return {"status": False}






