# ✅ umaralertbot/fomo_scanner/fomo_main.py

from fomo_scanner.fomo_core import detect_fomo_trades

def check_fomo_signals():
    try:
        results = detect_fomo_trades()
        if results:
            return {
                "status": True,
                "message": results.get("alert"),
                "confidence": results.get("confidence", "low")
            }
        else:
            return {"status": False}
    except Exception as e:
        print(f"[FOMO Scanner Error] {e}")
        return {"status": False}



