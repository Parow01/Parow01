import requests

EXCHANGE_WALLETS = {
    "Binance": ["0x3f5CE5FBFe3E9af3971dD833D26BA9b5C936f0bE"],
    "Coinbase": ["0x503828976D22510aad0201ac7EC88293211D23Da"],
    "Kraken": ["0x0A869d79a7052C7f1b55a8ebabbea3420F0D1E13"]
}

ETHERSCAN_API_KEY = "YourFreeEtherscanAPIKey"  # Replace with actual free key

def get_wallet_activity(wallet_address: str) -> list:
    url = f"https://api.etherscan.io/api"
    params = {
        "module": "account",
        "action": "txlist",
        "address": wallet_address,
        "startblock": 9999999 - 1000,
        "endblock": 99999999,
        "sort": "desc",
        "apikey": ETHERSCAN_API_KEY
    }
    try:
        response = requests.get(url, params=params, timeout=10)
        result = response.json()
        if result["status"] == "1":
            return result["result"]
    except Exception:
        pass
    return []

def detect_hotwallet_activity() -> dict | None:
    alerts = []
    for exchange, wallets in EXCHANGE_WALLETS.items():
        for wallet in wallets:
            txs = get_wallet_activity(wallet)
            if txs:
                recent_tx = txs[0]
                value_eth = int(recent_tx["value"]) / 1e18
                if value_eth > 1000:
                    alerts.append(f"🔥 Large TX from {exchange}: {value_eth:.2f} ETH → {recent_tx['to']}")
    if alerts:
        return {
            "type": "hotwallet",
            "alert": "\n".join(alerts),
            "confidence": "medium"
        }
    return None
