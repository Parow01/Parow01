# filter_core.py

def passes_filter(alert: dict) -> bool:
    """
    Filters alerts based on type, confidence level, and blueprint rules.
    """
    alert_type = alert.get("type", "")
    confidence = alert.get("confidence", "")
    direction = alert.get("direction", "")

    # General rule: only high or medium confidence alerts pass
    if confidence not in ["high", "medium"]:
        return False

    # Specific blueprint filters
    if alert_type == "whale" and confidence == "high":
        return True

    if alert_type == "netflow" and direction == "bullish":
        return True

    if alert_type == "reserves" and direction in ["bullish", "bearish"]:
        return True

    if alert_type == "sentiment" and confidence == "high":
        return True

    if alert_type == "strategy" and confidence == "high":
        return True

    if alert_type == "fomo" and confidence == "high":
        return True

    # Default: pass medium confidence alerts from key types
    if alert_type in ["liquidation", "funding", "confluence"]:
        return True

    return False
