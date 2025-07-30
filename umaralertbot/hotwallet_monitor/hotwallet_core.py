# ✅ umaralertbot/hotwallet_monitor/hotwallet_core.py

import requests
import logging
import os
from dotenv import load_dotenv
from alert_engine.send_alert import send_telegram_alert

load_dotenv()

ETHERSCAN_API_KEY = os.getenv("ETHERSCAN_API_KEY")  # Load from .env

EXCHANGE_WALLETS = {
    "Binance": ["0x3f5CE5FBFe3E9af3971dD833D26BA9b5C936f0bE"],
    "Coinbase": ["0x503828976D22510aad0201ac7EC88293211D23Da"],
    "Kraken": ["0x0A869d79a7052C7f1b55a8ebabbea3420F0D1E13"]
}

def get_wallet_activity(wallet_address: str) -> list:
    try:
        url = "https://api.etherscan.io/api"
        params = {
            "module": "account",
            "action": "txlist",
            "address": wallet_address,
            "startblock": 9999999 - 1000,
            "endblock": 99999999,
            "sort": "desc",
            "apikey": ETHERSCAN_API_KEY
        }
        response = requests.get(url, params=params, timeout=10)
        data = response.json()
        if data["status"] == "1":
            return data["result"]
    except Exception as e:
        logging.warning(f"[HotWallet] API error for {wallet_address}: {e}")
    return []

def check_hotwallet_activity():
    try:
        logging.info("🔍 Checking exchange hot wallet activity...")
        alerts = []

        for exchange, wallets in EXCHANGE_WALLETS.items():
            for wallet in wallets:
                txs = get_wallet_activity(wallet)
                if txs:
                    latest_tx = txs[0]
                    value_eth = int(latest_tx["value"]) / 1e18
                    to_addr = latest_tx["to"]
                    if value_eth > 1000:  # Threshold for large tx
                        alerts.append(
                            f"<b>🔥 Large TX from {exchange}</b>\n"
                            f"💸 <b>Amount:</b> {value_eth:.2f} ETH\n"
                            f"📥 <b>To:</b> {to_addr}\n"
                        )

        if alerts:
            message = "<b>🔁 Exchange Hot Wallet Alert</b>\n\n" + "\n".join(alerts)
            send_telegram_alert(message)

    except Exception as e:
        logging.error(f"[HotWallet] Unexpected error: {e}")

