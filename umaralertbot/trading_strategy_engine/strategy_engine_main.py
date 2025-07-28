# umaralertbot/trading_strategy_engine/strategy_engine_main.py

import logging
from utils.helper_functions import load_token_data, calculate_indicators

logger = logging.getLogger(__name__)

def apply_strategy(token_data):
    """
    Example strategy: EMA crossover + volume spike.
    """
    try:
        df = calculate_indicators(token_data)
        if df is None or df.empty:
            logger.warning("Token data is empty or invalid.")
            return []

        signals = []
        for symbol, data in df.groupby("symbol"):
            recent = data.iloc[-1]
            if recent["ema_fast"] > recent["ema_slow"] and recent["volume_change"] > 2:
                signals.append(symbol)

        logger.info(f"Generated signals for: {signals}")
        return signals

    except Exception as e:
        logger.error(f"Error in apply_strategy: {e}")
        return []
