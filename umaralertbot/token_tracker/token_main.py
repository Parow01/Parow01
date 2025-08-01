import asyncio
import logging
from apscheduler.schedulers.background import BackgroundScheduler
from token_tracker.token_core import track_tokens
from alert_engine.alert_dispatcher import dispatch_alert

# ✅ Wrapper to safely run async inside sync scheduler
def run_token_tracker():
    try:
        asyncio.run(_run_token_logic())
    except Exception as e:
        logging.error(f"[Token Tracker Error] {e}")

# ✅ Schedule this from main.py
def start_token_tracker(scheduler: BackgroundScheduler):
    scheduler.add_job(run_token_tracker, "interval", minutes=3)
    logging.info("✅ Token Tracker job added to scheduler.")

# ✅ Async logic stays here
async def _run_token_logic():
    results = await track_tokens()
    if results:
        for alert in results:
            await dispatch_alert(alert)


