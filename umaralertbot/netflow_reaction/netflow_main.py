# ✅ umaralertbot/netflow_engine/netflow_main.py

import logging
from netflow_engine.netflow_core import run_netflow_engine

def start_netflow_engine(scheduler):
    try:
        scheduler.add_job(
            run_netflow_engine,
            trigger='interval',
            seconds=90,
            id='netflow_engine_job',
            replace_existing=True
        )
        logging.info("✅ Netflow Engine scheduled successfully.")
    except Exception as e:
        logging.error(f"❌ Failed to start Netflow Engine: {e}")
