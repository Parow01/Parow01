# smartlist_core.py

import requests
import time

SMART_WHALE_ADDRESSES = [
    "0x28C6c06298d514Db089934071355E5743bf21d60",  # Binance 14
    "0x564286362092D8e7936f0549571a803B203aAceD",  # Smart Money 1
    "0x267be1c1d684f78cb4f6a176c4911b741e4ffdc0",  # Smart Money 2
]

ETHERSCAN_API_KEY = "P42VPVV2CH2JGXZ4PYMVFR5X9YGKJQVI9"  # Your Etherscan API key

def fetch_smart_whale_activity():
    alerts = []

    for address in SMART_WHALE_ADDRESSES:
        url = f"https://api.etherscan.io/api?module=account&action=txlist&address={address}&sort=desc&apikey={ETHERSCAN_API_KEY}"
        try:
            response = requests.get(url)
            data = response.json()
            if data["status"] == "1":
                latest_tx = data["result"][0]
                value_eth = int(latest_tx["value"]) / 1e18
                to_addr = latest_tx["to"]
                from_addr = latest_tx["from"]
                timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(latest_tx["timeStamp"])))

                alert = (
                    f"🧠 Smart Whale Activity Detected\n"
                    f"From: {from_addr}\n"
                    f"To: {to_addr}\n"
                    f"Value: {value_eth:.2f} ETH\n"
                    f"Time: {timestamp}"
                )
                alerts.append(alert)
        except Exception as e:
            print(f"[smartlist_core] Error fetching activity for {address}: {e}")

    return alerts


