# umaralertbot/filter_engine/filter_main.py

import logging

class AlertFilterEngine:
    def __init__(self, blacklist=None, min_usd_volume=100000):
        self.logger = logging.getLogger(__name__)
        self.blacklist = blacklist if blacklist else []
        self.min_usd_volume = min_usd_volume

    def is_blacklisted(self, token_symbol):
        return token_symbol.upper() in self.blacklist

    def is_large_transaction(self, amount_usd):
        return amount_usd >= self.min_usd_volume

    def filter_alert(self, token_symbol, amount_usd):
        if self.is_blacklisted(token_symbol):
            self.logger.info(f"{token_symbol} is blacklisted. Alert skipped.")
            return False
        if not self.is_large_transaction(amount_usd):
            self.logger.info(f"{token_symbol} transaction ${amount_usd} is too small. Skipped.")
            return False
        return True
