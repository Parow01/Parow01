# alert_engine_main.py

from alert_engine.alert_router import process_alert

def send_alert(alert: dict):
    """
    External interface for engines to trigger alerts.
    """
    process_alert(alert)

