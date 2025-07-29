# ✅ umaralertbot/liquidation_heatmap/heatmap_main.py

import logging
from liquidation_heatmap.liquidation_checker import check_liquidation_cluster

def run_liquidation_job():
    try:
        alert = check_liquidation_cluster()
        if alert:
            logging.info(f"💥 [Liquidation Heatmap Alert] {alert['alert']}")
            # In future: send_telegram_alert(alert['alert'])
        else:
            logging.info("📉 [Liquidation Heatmap] No significant liquidations.")
    except Exception as e:
        logging.error(f"❌ [Liquidation Heatmap Error] {e}")

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
        logging.error(f"❌ Failed to start Liquidation Heatmap: {e}")
