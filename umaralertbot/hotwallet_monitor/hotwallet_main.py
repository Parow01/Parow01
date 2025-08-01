# ✅ umaralertbot/hotwallet_monitor/hotwallet_main.py

import logging
from apscheduler.triggers.interval import IntervalTrigger
from hotwallet_monitor.hotwallet_core import check_hotwallet_activity

def start_hotwallet_monitor(scheduler):
    scheduler.add_job(
        check_hotwallet_activity,
        trigger=IntervalTrigger(minutes=6),
        id="job_hotwallet_monitor",
        replace_existing=True
    )
    logging.info("✅ Hot Wallet Monitor job added to scheduler.")






