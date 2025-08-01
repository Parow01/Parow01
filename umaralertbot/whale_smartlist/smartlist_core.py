import os
import logging
from dotenv import load_dotenv
import time
from utils.etherscan_helper import get_wallet_transactions
from alert_engine.send_alert import send_telegram_alert

load_dotenv()
ETHERSCAN_API_KEY = os.getenv("ETHERSCAN_API_KEY")

# ✅ Known tagged addresses
SMART_WHALE_ADDRESSES = {
    "Binance 14": "0x28C6c06298d514Db089934071355E5743bf21d60",
    "Smart Money 1": "0x564286362092D8e7936f0549571a803B203aAceD",
    "Smart Money 2": "0x267be1c1d684f78cb4f6a176c4911b741e4ffdc0",
}

THRESHOLD_ETH = 100

def check_smart_wallets():
    alerts = []

    for label, address in SMART_WHALE_ADDRESSES.items():
        try:
            txs = get_wallet_transactions(address)
            if not txs:
                continue

            latest = txs[0]
            value_eth = int(latest["value"]) / 1e18
            if value_eth >= THRESHOLD_ETH:
                timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(latest["timeStamp"])))
                alert = (
                    f"🧠 <b>Smart Whale Activity Detected</b>\n"
                    f"👤 <b>Wallet:</b> {label}\n"
                    f"💸 <b>Value:</b> {value_eth:.2f} ETH\n"
                    f"📤 <b>To:</b> {latest['to']}\n"
                    f"🕒 <b>Time:</b> {timestamp}\n"
                    f"🔗 <a href='https://etherscan.io/tx/{latest['hash']}'>View Tx</a>"
                )
                alerts.append(alert)
        except Exception as e:
            logging.error(f"[smartlist_core] Error fetching {label}: {e}")

    if alerts:
        send_telegram_alert("\n\n".join(alerts))



