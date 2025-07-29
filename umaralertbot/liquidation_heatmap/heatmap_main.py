import logging
from liquidation_heatmap.heatmap_core import run_liquidation_job

def start_liquidation_heatmap(scheduler):
    try:
        scheduler.add_job(
            run_liquidation_job,
            trigger='interval',
            seconds=90,
            id='liquidation_heatmap_job',
            replace_existing=True
        )
        logging.info("✅ Liquidation Heatmap engine scheduled successfully.")
    except Exception as e:
        logging.error(f"❌ Failed to start liquidation heatmap: {e}")

