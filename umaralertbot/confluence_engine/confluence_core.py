# ✅ umaralertbot/confluence_engine/confluence_core.py

def evaluate_confluence(signals: list) -> dict | None:
    """
    Evaluates a list of signals from different modules and determines if confluence is strong.
    """
    if not signals or len(signals) < 2:
        return None  # Not enough signals for confluence

    types = [sig["type"] for sig in signals if "type" in sig]

    # Simple logic: If 2+ distinct types occur close together → trigger confluence
    unique_types = set(types)

    if len(unique_types) >= 2:
        alert_lines = [sig["alert"] for sig in signals if "alert" in sig]
        return {
            "type": "confluence",
            "alert": "📊 Confluence Detected:\n\n" + "\n\n".join(alert_lines),
            "confidence": "very high"
        }

    return None
