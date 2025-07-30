import json

def try_json_parse(data: str):
    try:
        return json.loads(data)
    except Exception:
        return {}

def clamp(value, min_val, max_val):
    return max(min_val, min(value, max_val))
