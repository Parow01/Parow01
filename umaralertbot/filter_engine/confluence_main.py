from whale_engine.smartlist import check_smartlist_activity
from netflow_engine.netflow import analyze_netflow
from liquidation_heatmap.liquidation_alert import check_liquidation_clusters
from reserve_monitor.wallet_monitor import check_exchange_reserves

def check_confluence() -> dict | None:
    """
    Combines signals and filters based on confluence.
    """
    results = []

    smartlist_signal = check_smartlist_activity()
    if smartlist_signal:
        results.append(smartlist_signal)

    netflow_signal = analyze_netflow()
    if netflow_signal:
        results.append(netflow_signal)

    reserve_signal = check_exchange_reserves()
    if reserve_signal:
        results.append(reserve_signal)

    liquidation_signal = check_liquidation_clusters()
    if liquidation_signal:
        results.append(liquidation_signal)

    if len(results) >= 3:
        strength = "high"
    elif len(results) == 2:
        strength = "medium"
    else:
        return None  # not enough confluence

    direction = "bullish" if sum("bullish" in s["alert"].lower() for s in results) > 1 else "bearish"

    return {
        "direction": direction,
        "strength": strength,
        "alerts": results
    }
