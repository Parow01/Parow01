# ✅ umaralertbot/liquidation_heatmap/heatmap_main.py

from apscheduler.schedulers.background import BackgroundScheduler
from liquidation_heatmap.heatmap_core import check_liquidation_clusters

def start_liquidation_heatmap():
    scheduler = BackgroundScheduler()
    scheduler.add_job(check_liquidation_clusters, 'interval', minutes=5)
    scheduler.start()


