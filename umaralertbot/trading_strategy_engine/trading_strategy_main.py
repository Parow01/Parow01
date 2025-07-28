# umaralertbot/trading_strategy_engine/trading_strategy_main.py

def moving_average_strategy(prices, short_window=5, long_window=20):
    """
    A simple moving average crossover strategy.
    Returns buy/sell/hold signals.
    """
    if len(prices) < long_window:
        return "hold"

    short_ma = sum(prices[-short_window:]) / short_window
    long_ma = sum(prices[-long_window:]) / long_window

    if short_ma > long_ma:
        return "buy"
    elif short_ma < long_ma:
        return "sell"
    else:
        return "hold"
