# ✅ umaralertbot/liquidation_heatmap/heatmap_main.py

from liquidation_heatmap.heatmap_core import check_liquidation_clusters

def start_liquidation_heatmap(scheduler):
    def job():
        try:
            check_liquidation_clusters()
        except Exception as e:
            print(f"❌ Error in liquidation heatmap job: {e}")

    scheduler.add_job(job, 'interval', minutes=5)




