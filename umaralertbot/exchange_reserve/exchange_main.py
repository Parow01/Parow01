from apscheduler.schedulers.background import BackgroundScheduler
from exchange_reserve.exchange_core import check_exchange_reserves

def start_exchange_reserve_monitor():
    scheduler = BackgroundScheduler(timezone="Africa/Lagos")
    scheduler.add_job(check_exchange_reserves, 'interval', minutes=7)
    scheduler.start()
