# alert_guard.py

from datetime import datetime, timedelta

recent_alerts = {}

def is_duplicate(alert_text: str, cooldown_minutes: int = 5) -> bool:
    """
    Prevents duplicate alerts by checking if the same text was sent recently.
    """
    now = datetime.utcnow()
    last_sent = recent_alerts.get(alert_text)

    if last_sent and now - last_sent < timedelta(minutes=cooldown_minutes):
        return True

    recent_alerts[alert_text] = now
    return False

