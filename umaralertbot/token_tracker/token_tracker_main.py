import asyncio
from token_tracker.token_core import track_tokens
from alert_engine.alert_dispatcher import dispatch_alert
from apscheduler.schedulers.background import BackgroundScheduler

def start_token_tracker():
    scheduler = BackgroundScheduler(timezone="UTC")
    scheduler.add_job(run_token_tracker, "interval", minutes=3)
    scheduler.start()
    print("[token_tracker] Tracker scheduled every 3 mins")

def run_token_tracker():
    asyncio.run(_run_token_logic())

async def _run_token_logic():
    results = await track_tokens()
    if results:
        for alert in results:
            await dispatch_alert(alert)


