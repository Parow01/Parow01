# ✅ umaralertbot/confluence_engine/confluence_main.py

import logging
from confluence_engine.confluence_core import evaluate_confluence
from alert_manager.dispatch import send_alert

# Import core engines
from whale_screener.screener_core import fetch_and_process_screener_data
from fomo_scanner.fomo_core import scan_fomo_trades
from liquidation_heatmap.heatmap_core import check_liquidation_clusters
from funding_rate_monitor.funding_rate_monitor_main import monitor_funding_rates
from netflow_reaction.netflow_core import analyze_netflow
from whale_smartlist.smartlist_core import detect_whale_activity
from hotwallet_monitor.hotwallet_core import get_hotwallet_activity

def run_confluence_engine():
    try:
        signals = []

        # Run each core engine manually and gather signals (if any)
        for engine in [
            fetch_and_process_screener_data,
            scan_fomo_trades,
            check_liquidation_clusters,
            monitor_funding_rates,
            analyze_netflow,
            detect_whale_activity,
            get_hotwallet_activity
        ]:
            result = engine()
            if result:
                signals.append(result)

        # Run confluence check
        final_alert = evaluate_confluence(signals)
        if final_alert:
            send_alert(final_alert)

        logging.info("🧠 Confluence Engine checked successfully.")

    except Exception as e:
        logging.error(f"❌ Confluence Engine Error: {e}")

def start_confluence_engine(scheduler):
    try:
        scheduler.add_job(
            run_confluence_engine,
            trigger='interval',
            seconds=150,
            id='confluence_engine_job',
            replace_existing=True
        )
        logging.info("✅ Confluence Engine scheduled successfully.")
    except Exception as e:
        logging.error(f"❌ Failed to schedule Confluence Engine: {e}")




