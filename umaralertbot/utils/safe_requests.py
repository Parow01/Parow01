# umaralertbot/utils/safe_requests.py

import requests
import time

def safe_get(url, params=None, headers=None, max_retries=3, timeout=10):
    """
    A safe wrapper around requests.get to handle retry logic gracefully.
    """
    attempt = 0
    while attempt < max_retries:
        try:
            response = requests.get(url, params=params, headers=headers, timeout=timeout)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            print(f"[safe_get] Error: {e}. Retrying ({attempt + 1}/{max_retries})...")
            time.sleep(2)
            attempt += 1
    return None
