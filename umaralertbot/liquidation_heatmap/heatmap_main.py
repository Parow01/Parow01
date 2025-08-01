# ✅ umaralertbot/liquidation_heatmap/heatmap_main.py

from liquidation_heatmap.heatmap_core import check_liquidation_clusters
from apscheduler.schedulers.background import BackgroundScheduler
import logging

# ✅ Background job scheduler (used in main.py)
def start_liquidation_heatmap_monitor(scheduler: BackgroundScheduler):
    def job():
        try:
            check_liquidation_clusters()
        except Exception as e:
            print(f"❌ Error in liquidation heatmap job: {e}")
    scheduler.add_job(job, 'interval', minutes=5)

# ✅ Confluence-compatible function (used in alert_engine)
def check_liquidation_heatmap():
    try:
        result = check_liquidation_clusters()
        if result:
            return {
                "status": True,
                "message": result.get("alert"),
                "confidence": result.get("confidence", "medium")
            }
        else:
            return {"status": False}
    except Exception as e:
        logging.error(f"[Liquidation Heatmap Error] {e}")
        return {"status": False}






