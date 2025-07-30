# ✅ umaralertbot/confluence_engine/confluence_main.py

import logging
from apscheduler.schedulers.background import BackgroundScheduler
from whale_screener.whale_core import detect_whale_activity
from fomo_scanner.fomo_core import fetch_and_process_fomo_data
from funding_rate_monitor.funding_core import analyze_funding_rates
from liquidation_heatmap.heatmap_core import check_liquidation_clusters
from confluence_engine.confluence_utils import send_confluence_alert

def check_confluence():
    try:
        logging.info("🔎 Checking for Confluence Signals...")

        whale_alert = detect_whale_activity()
        fomo_alert = fetch_and_process_fomo_data()
        funding_alert = analyze_funding_rates()
        heatmap_alert = check_liquidation_clusters()

        bullish_signals = [
            whale_alert.get("direction") == "bullish",
            fomo_alert.get("direction") == "bullish",
            funding_alert.get("direction") == "bullish",
            heatmap_alert.get("direction") == "bullish",
        ]
        bearish_signals = [
            whale_alert.get("direction") == "bearish",
            fomo_alert.get("direction") == "bearish",
            funding_alert.get("direction") == "bearish",
            heatmap_alert.get("direction") == "bearish",
        ]

        if bullish_signals.count(True) >= 3:
            message = (
                "<b>📊 Smart Confluence Alert</b>\n\n"
                "🔵 Bullish sentiment detected across multiple engines:\n"
                f"{whale_alert['alert']}\n"
                f"{fomo_alert['alert']}\n"
                f"{funding_alert['alert']}\n"
                f"{heatmap_alert['alert']}"
            )
            send_confluence_alert(message)

        elif bearish_signals.count(True) >= 3:
            message = (
                "<b>📊 Smart Confluence Alert</b>\n\n"
                "🔴 Bearish sentiment detected across multiple engines:\n"
                f"{whale_alert['alert']}\n"
                f"{fomo_alert['alert']}\n"
                f"{funding_alert['alert']}\n"
                f"{heatmap_alert['alert']}"
            )
            send_confluence_alert(message)

    except Exception as e:
        logging.error(f"❌ Error in confluence checker: {e}")

def start_confluence_engine():
    scheduler = BackgroundScheduler()
    scheduler.add_job(check_confluence, "interval", minutes=4)
    scheduler.start()
    logging.info("✅ Confluence engine started.")




