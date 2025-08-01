import os
import requests

API_KEYS = {
    "ethereum": os.getenv("ETHERSCAN_API_KEY"),
    "bsc": os.getenv("BSCSCAN_API_KEY"),
    "arbitrum": os.getenv("ARBITRUM_API_KEY"),
    "optimism": os.getenv("OPTIMISM_API_KEY")
}

API_URLS = {
    "ethereum": "https://api.etherscan.io/api",
    "bsc": "https://api.bscscan.com/api",
    "arbitrum": "https://api.arbiscan.io/api",
    "optimism": "https://api-optimistic.etherscan.io/api"
}

def get_transactions(address, chain="ethereum", action="txlist", startblock=0, endblock=99999999, sort="desc"):
    """Fetches transaction history for a given address on specified chain"""
    api_key = API_KEYS.get(chain)
    base_url = API_URLS.get(chain)

    if not api_key or not base_url:
        raise ValueError(f"No API key or URL configured for chain: {chain}")

    params = {
        "module": "account",
        "action": action,
        "address": address,
        "startblock": startblock,
        "endblock": endblock,
        "sort": sort,
        "apikey": api_key
    }

    response = requests.get(base_url, params=params)
    response.raise_for_status()
    return response.json()
