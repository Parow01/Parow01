import logging
from apscheduler.triggers.interval import IntervalTrigger
from whale_smartlist.smartlist_core import check_smart_wallets

def start_smartlist_monitor(scheduler):
    scheduler.add_job(
        check_smart_wallets,
        trigger=IntervalTrigger(minutes=10),
        id="job_smartlist_monitor",
        replace_existing=True
    )
    logging.info("✅ Smartlist Monitor job added to scheduler.")


