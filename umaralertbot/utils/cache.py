# umaralertbot/utils/cache.py

_cache = {}

def set_cache(key: str, value: any, ttl_seconds: int = 60):
    from time import time
    _cache[key] = (value, time() + ttl_seconds)

def get_cache(key: str):
    from time import time
    value, expiry = _cache.get(key, (None, 0))
    if time() < expiry:
        return value
    return None
