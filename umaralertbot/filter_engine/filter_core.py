# filter_core.py

def apply_confluence_filters(signals: list[dict]) -> list[dict]:
    """
    Apply confluence logic to incoming alerts.

    A signal must meet at least 2 out of 3 filters to pass:
    - Has confidence level
    - Has direction (bullish or bearish)
    - Comes from specific 'smart' modules
    """
    passed = []

    for signal in signals:
        score = 0

        if signal.get("confidence"):
            score += 1
        if signal.get("direction"):
            score += 1
        if signal.get("type") in [
            "whale", "fomo", "netflow", "reserves", "funding", "heatmap", "sentiment"
        ]:
            score += 1

        if score >= 2:
            passed.append(signal)

    return passed
