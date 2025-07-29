# alert_router.py

from filter_engine.filter_main import run_filter_engine

def process_alert(alert: dict):
    """
    Central hub: Receives raw alert from any engine and passes it through the filter engine.
    """
    if alert:
        run_filter_engine(alert)
