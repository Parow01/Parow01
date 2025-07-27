def filter_signals(signals: list[dict]) -> dict | None:
    """
    Accepts a list of signals and filters for confluence.
    Returns one final alert dict or None.
    """
    if not signals:
        return None

    bullish_signals = [s for s in signals if s.get("direction") == "bullish"]
    bearish_signals = [s for s in signals if s.get("direction") == "bearish"]

    if len(bullish_signals) >= 2:
        return {
            "strength": "high" if len(bullish_signals) == 3 else "medium",
            "direction": "bullish",
            "alerts": bullish_signals
        }

    if len(bearish_signals) >= 2:
        return {
            "strength": "high" if len(bearish_signals) == 3 else "medium",
            "direction": "bearish",
            "alerts": bearish_signals
        }

    return None
