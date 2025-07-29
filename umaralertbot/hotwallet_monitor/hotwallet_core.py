# ✅ umaralertbot/hotwallet_monitor/hotwallet_core.py

import random

# Simulated database of exchange wallets
EXCHANGE_WALLETS = {
    "Binance": ["0xBinanceWallet1", "0xBinanceWallet2"],
    "OKX": ["0xOKXWallet1"],
    "Coinbase": ["0xCoinbaseWallet"]
}

def check_exchange_wallet_flows() -> dict | None:
    """
    Simulate detecting large inflows/outflows from exchange wallets.
    In production, you'd replace this with on-chain API or scrape.
    """
    exchange = random.choice(list(EXCHANGE_WALLETS.keys()))
    action = random.choice(["deposit", "withdrawal"])
    amount = random.randint(10, 120)

    if amount >= 50:
        emoji = "🏦" if action == "deposit" else "🚪"
        return {
            "type": "exchange_wallet",
            "alert": f"{emoji} ${amount}M {action.title()} on {exchange} Exchange Detected!",
            "exchange": exchange,
            "amount": amount
        }

    return None
