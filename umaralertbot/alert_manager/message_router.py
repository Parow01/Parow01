import logging
from alert_manager.alert_dispatcher import send_telegram_alert

def route_alert(signal):
    """
    Accepts a signal dictionary and sends a Telegram alert.
    Signal must contain at least:
        - type: engine name (e.g. whale_screener, fomo_scanner)
        - alert: message string
        - confidence: low, medium, high
    """
    try:
        if not isinstance(signal, dict):
            raise ValueError("Signal must be a dictionary")

        alert_type = signal.get("type", "general").replace("_", " ").title()
        alert_msg = signal.get("alert", "🚨 No message provided")
        confidence = signal.get("confidence", "unknown").capitalize()

        message = (
            f"<b>🚨 {alert_type} Alert</b>\n\n"
            f"{alert_msg}\n\n"
            f"<b>Confidence:</b> {confidence}"
        )

        send_telegram_alert(message)
        logging.info(f"✅ Routed alert from {alert_type}")

    except Exception as e:
        logging.error(f"❌ Error routing alert: {e}")
