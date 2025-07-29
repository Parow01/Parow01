# filter_main.py

from filter_engine.filter_core import passes_filter
from alert_manager.alert_handler import send_alert_to_telegram

def run_filter_engine(alert: dict):
    """
    Pass the alert through the filter engine before sending.
    """
    if passes_filter(alert):
        send_alert_to_telegram(alert)

