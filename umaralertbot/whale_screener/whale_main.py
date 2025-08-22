from whale_screener.whale_core import run_screener
import logging

def start_whale_screener():
    """
    Runs the Whale Screener engine.
    """
    logging.info("🔁 Starting Whale Screener Engine...")
    result = run_screener()

    if result:
        logging.info("✅ Whale Screener finished successfully.")
        return result
    else:
        logging.warning("⚠️ Whale Screener returned no data.")
        return None


 
