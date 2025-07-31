import time
from typing import List, Dict

from whale_screener.whale_core import detect_whale_activity
from fomo_scanner.fomo_main import check_fomo_signals
from funding_rate_monitor.funding_main import check_funding_rate_skew
from liquidation_heatmap.heatmap_main import check_liquidation_heatmap
from confluence_engine.confluence_main import start_confluence_engine
from netflow_reaction.netflow_main import detect_netflow_reaction
from exchange_reserve.reserve_main import detect_reserve_shift
from hotwallet_monitor.hotwallet_main import detect_hotwallet_movement
from whale_sentiment.sentiment_main import start_sentiment_engine
from whale_smartlist.smartlist_main import start_smartlist_monitor
from token_tracker.token_main import start_token_monitor
from trading_strategy_engine.strategy_main import run_strategy_engine

alert_history = []

def collect_all_alerts() -> List[Dict]:
    """
    Calls all active engines, filters unique and relevant alerts.
    """
    raw_alerts = []

    modules = [
        detect_whale_activity,
        check_fomo_signals,
        check_funding_rate_skew,
        check_liquidation_heatmap,
        start_confluence_engine,
        detect_netflow_reaction,
        detect_reserve_shift,
        detect_hotwallet_movement,
        evaluate_whale_sentiment,
        scan_smartlist_trades,
        detect_token_spike,
        run_strategy_engine
    ]

    for module in modules:
        try:
            result = module()
            if result:
                if isinstance(result, list):
                    raw_alerts.extend(result)
                else:
                    raw_alerts.append(result)
        except Exception as e:
            print(f"[alert_engine] Error in {module.__name__}: {e}")

    return filter_clean_alerts(raw_alerts)

def filter_clean_alerts(alerts: List[Dict]) -> List[Dict]:
    """
    Applies confidence threshold and prevents duplicate spam.
    """
    final_alerts = []
    seen_signatures = set()

    for alert in alerts:
        key = alert.get("type", "") + alert.get("alert", "")
        if key in seen_signatures:
            continue
        seen_signatures.add(key)

        # Basic filter: Allow only high or medium alerts, avoid low confidence
        if alert.get("confidence", "medium") in ["high", "medium"]:
            final_alerts.append(alert)

    return final_alerts

