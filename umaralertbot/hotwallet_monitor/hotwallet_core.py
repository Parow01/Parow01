# ✅ hotwallet_monitor/hotwallet_core.py
import logging
from utils.etherscan_helper import get_wallet_transactions
from alert_engine.send_alert import send_telegram_alert

# ✅ Predefined exchange wallets
EXCHANGE_WALLETS = {
    "Binance": ["0x3f5CE5FBFe3E9af3971dD833D26BA9b5C936f0bE"],
    "Coinbase": ["0x503828976D22510aad0201ac7EC88293211D23Da"],
    "Kraken": ["0x0A869d79a7052C7f1b55a8ebabbea3420F0D1E13"]
}

# ✅ Known exchange receiving wallets to filter out internal tx
KNOWN_EXCHANGE_DESTINATIONS = set(sum(EXCHANGE_WALLETS.values(), []))

TX_ETH_THRESHOLD = 1000  # ≈ $3M+

def check_hotwallet_activity():
    try:
        logging.info("🔍 [Hotwallet] Checking hot wallet activity...")
        alerts = []

        for exchange, wallets in EXCHANGE_WALLETS.items():
            for wallet in wallets:
                transactions = get_wallet_transactions(wallet)
                if not transactions:
                    continue

                for tx in transactions:
                    if tx.get("value_eth", 0) >= TX_ETH_THRESHOLD:
                        if tx["to"].lower() in KNOWN_EXCHANGE_DESTINATIONS:
                            continue  # Skip internal transfers

                        alerts.append(
                            f"<b>🔥 Large Transfer from {exchange}</b>\n"
                            f"💸 <b>Amount:</b> {tx['value_eth']:.2f} ETH\n"
                            f"📥 <b>To:</b> {tx['to']}\n"
                            f"🔗 <a href='https://etherscan.io/tx/{tx['hash']}'>View TX</a>"
                        )
                        break  # Only alert on most recent valid large tx

        if alerts:
            message = "<b>🚨 Hot Wallet Movement Detected</b>\n\n" + "\n\n".join(alerts)
            send_telegram_alert(message)
        else:
            logging.info("✅ [Hotwallet] No large movement detected.")

    except Exception as e:
        logging.error(f"[Hotwallet] Error in check_hotwallet_activity(): {e}")


