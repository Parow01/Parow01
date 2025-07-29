import logging
from confluence_engine.confluence_core import run_confluence_engine

def start_confluence_engine(scheduler):
    try:
        scheduler.add_job(
            run_confluence_engine,
            trigger='interval',
            seconds=90,
            id='confluence_engine_job',
            replace_existing=True
        )
        logging.info("✅ Confluence Engine scheduled successfully.")
    except Exception as e:
        logging.error(f"❌ Failed to start Confluence Engine: {e}")



