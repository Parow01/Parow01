import logging
from apscheduler.schedulers.background import BackgroundScheduler
from whale_engine.whale_core import fetch_and_process_whales

# Configure logging for this module
logger = logging.getLogger(__name__)

def start_whale_engine(scheduler: BackgroundScheduler):
    """
    Starts the whale alert job on the provided scheduler.

    Args:
        scheduler (BackgroundScheduler): The scheduler instance to register the job with.
    """
    try:
        scheduler.add_job(
            fetch_and_process_whales,
            trigger="interval",
            seconds=60,
            id="whale_alert_job",
            replace_existing=True
        )
        logger.info("✅ Whale engine scheduled successfully.")
    except Exception as e:
        logger.error(f"❌ Failed to schedule whale engine: {e}")
