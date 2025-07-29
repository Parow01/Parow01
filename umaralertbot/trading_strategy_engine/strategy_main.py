# strategy_main.py

from trading_strategy_engine.strategy_core import generate_trading_signal
from alert_manager.alert_handler import send_alert_to_telegram

def start_strategy_engine():
    signal = generate_trading_signal()
    if signal:
        send_alert_to_telegram(signal)
