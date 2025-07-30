# umaralertbot/utils/time_utils.py

from datetime import datetime, timezone

def get_utc_timestamp() -> int:
    return int(datetime.now(timezone.utc).timestamp())

def get_human_time() -> str:
    return datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")

