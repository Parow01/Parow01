# ✅ umaralertbot/whale_screener/screener_main.py

from whale_screener.screener_core import fetch_whale_data, analyze_whale_patterns

def detect_whale_activity():
    try:
        data = fetch_whale_data()
        alerts = analyze_whale_patterns(data)
        return alerts
    except Exception as e:
        print(f"[Whale Screener] Error: {e}")
        return []



