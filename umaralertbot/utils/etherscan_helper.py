# ✅ umaralertbot/utils/etherscan_helper.py

import requests
import logging
import os
from dotenv import load_dotenv

load_dotenv()

ETHERSCAN_API_KEY = os.getenv("ETHERSCAN_API_KEY")

ETHERSCAN_DOMAINS = {
    "ethereum": "https://api.etherscan.io",
    "bsc": "https://api.bscscan.com",
    "polygon": "https://api.polygonscan.com",
    # Add more chains here if needed
}

def get_latest_transactions(wallet_address: str, chain: str = "ethereum", limit: int = 5):
    """
    Fetch recent transactions from Etherscan-compatible chains (Ethereum, BSC, Polygon, etc.)
    """
    try:
        base_url = ETHERSCAN_DOMAINS.get(chain.lower())
        if not base_url:
            logging.warning(f"[etherscan_helper] Unsupported chain: {chain}")
            return []

        url = f"{base_url}/api"
        params = {
            "module": "account",
            "action": "txlist",
            "address": wallet_address,
            "startblock": 0,
            "endblock": 99999999,
            "sort": "desc",
            "apikey": ETHERSCAN_API_KEY
        }
        response = requests.get(url, params=params, timeout=10)
        data = response.json()

        if data["status"] == "1":
            return data["result"][:limit]
        else:
            logging.warning(f"[etherscan_helper] No data for {wallet_address} on {chain}")
    except Exception as e:
        logging.error(f"[etherscan_helper] Error fetching tx for {wallet_address} on {chain}: {e}")
    return []

def is_contract(address: str, chain: str = "ethereum") -> bool:
    """
    Check if an address is a contract address
    """
    try:
        base_url = ETHERSCAN_DOMAINS.get(chain.lower())
        if not base_url:
            return False

        url = f"{base_url}/api"
        params = {
            "module": "contract",
            "action": "getsourcecode",
            "address": address,
            "apikey

