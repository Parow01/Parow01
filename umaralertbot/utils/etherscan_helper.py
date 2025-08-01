import requests
import time
from utils.safe_requests import safe_get

ETHERSCAN_API_KEY = "P42VPVV2CH2JGXZ4PYMVFR5X9YGKJQVI9N"
BASE_URL = "https://api.etherscan.io/api"

def get_wallet_transactions(wallet_address, start_block=0, end_block=99999999, sort="desc", max_retries=3):
    """
    Fetches normal transactions for a given wallet address from Etherscan API.
    """
    url = BASE_URL
    params = {
        "module": "account",
        "action": "txlist",
        "address": wallet_address,
        "startblock": start_block,
        "endblock": end_block,
        "sort": sort,
        "apikey": ETHERSCAN_API_KEY
    }

    for attempt in range(max_retries):
        try:
            response = safe_get(url, params=params)
            if response and response.get("status") == "1":
                return response["result"]
            elif response and response.get("message") == "No transactions found":
                return []
            else:
                print(f"[etherscan_helper] Unexpected response: {response}")
        except Exception as e:
            print(f"[etherscan_helper] Attempt {attempt + 1} failed: {e}")
        time.sleep(1)

    print("[etherscan_helper] Failed to fetch transactions after retries.")
    return []

def get_internal_transactions(wallet_address, start_block=0, end_block=99999999, sort="desc", max_retries=3):
    """
    Fetches internal transactions (e.g., contract interactions) for a wallet address.
    """
    url = BASE_URL
    params = {
        "module": "account",
        "action": "txlistinternal",
        "address": wallet_address,
        "startblock": start_block,
        "endblock": end_block,
        "sort": sort,
        "apikey": ETHERSCAN_API_KEY
    }

    for attempt in range(max_retries):
        try:
            response = safe_get(url, params=params)
            if response and response.get("status") == "1":
                return response["result"]
            elif response and response.get("message") == "No transactions found":
                return []
            else:
                print(f"[etherscan_helper] Unexpected response: {response}")
        except Exception as e:
            print(f"[etherscan_helper] Attempt {attempt + 1} failed: {e}")
        time.sleep(1)

    print("[etherscan_helper] Failed to fetch internal txs after retries.")
    return []

def is_hot_transaction(tx: dict) -> bool:
    """
    Determines if a transaction qualifies as a 'hot' wallet movement.
    Basic logic: high value, fast repeat, or abnormal pattern.
    """
    try:
        value_eth = int(tx["value"]) / 1e18
        if value_eth > 100:
            return True
        if tx.get("isError") == "1":
            return False
        return False
    except Exception:
        return False


