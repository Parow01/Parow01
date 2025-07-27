# umaralertbot/confluence_engine/confluence_main.py

import logging

class ConfluenceSignalEngine:
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def check_confluence_signal(self, token_flow_signal, netflow_signal, whale_signal):
        """
        Returns a confluence signal if at least two out of three signals match.
        """
        signals = [token_flow_signal, netflow_signal, whale_signal]
        signal_counts = {"bullish": 0, "bearish": 0}

        for signal in signals:
            if signal == "bullish":
                signal_counts["bullish"] += 1
            elif signal == "bearish":
                signal_counts["bearish"] += 1

        if signal_counts["bullish"] >= 2:
            self.logger.info("Confluence bullish signal detected.")
            return "bullish"
        elif signal_counts["bearish"] >= 2:
            self.logger.info("Confluence bearish signal detected.")
            return "bearish"
        else:
            self.logger.info("No strong confluence detected.")
            return "neutral"

