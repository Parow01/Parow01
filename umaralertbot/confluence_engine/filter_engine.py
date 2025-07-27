def get_signal_strength(signals: dict) -> str:
    """
    Determines the strength of combined signals.
    Returns: "high", "medium", or "low"
    """
    active = [k for k, v in signals.items() if v is not None]
    count = len(active)

    if count >= 3:
        return "high"
    elif count == 2:
        return "medium"
    elif count == 1:
        return "low"
    return "none"

def filter_alerts(signals: dict) -> dict | None:
    """
    Evaluates which signals are active and if they meet confluence threshold.
    Returns alert payload or None.
    """
    strength = get_signal_strength(signals)

    if strength == "high":
        return {
            "level": "🔴 HIGH",
            "messages": [v["alert"] for v in signals.values() if v],
        }

    elif strength == "medium":
        return {
            "level": "🟡 MEDIUM",
            "messages": [v["alert"] for v in signals.values() if v],
        }

    return None  # Low or no confluence
