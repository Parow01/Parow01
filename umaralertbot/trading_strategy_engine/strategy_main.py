def start_trading_engine(scheduler):
    from trading_strategy_engine.strategy_core import generate_trading_signal
    from alert_manager.alert_handler import send_alert_to_telegram

    def job():
        signal = generate_trading_signal()
        if signal:
            send_alert_to_telegram(signal)

    scheduler.add_job(job, trigger='interval', minutes=5, id='trading_engine_job', replace_existing=True)

