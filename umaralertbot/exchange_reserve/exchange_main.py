# ✅ umaralertbot/exchange_reserve/reserve_main.py

from apscheduler.schedulers.background import BackgroundScheduler
from exchange_reserve.reserve_core import analyze_exchange_reserves

def start_exchange_reserve_monitor():
    scheduler = BackgroundScheduler(timezone="Africa/Lagos")
    scheduler.add_job(analyze_exchange_reserves, 'interval', minutes=7)
    scheduler.start()

