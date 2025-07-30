# aggregator_core.py

def aggregate_signals(signals: list[dict]) -> list[dict]:
    """
    Merges and deduplicates raw signals from various engines.
    """
    seen = set()
    aggregated = []

    for signal in signals:
        uid = signal.get("type") + "_" + signal.get("alert")
        if uid not in seen:
            seen.add(uid)
            aggregated.append(signal)

    return aggregated
