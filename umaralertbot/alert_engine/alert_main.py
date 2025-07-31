import time
from alert_engine.alert_core import collect_all_alerts
from alert_manager.router_main import send_alert_to_telegram

def run_alert_engine():
    print("[AlertEngine] Starting master alert loop...")
    while True:
        alerts = collect_all_alerts()

        for alert in alerts:
            send_alert_to_telegram(alert)

        time.sleep(60)  # Wait before next polling


