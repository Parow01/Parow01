# ✅ umaralertbot/fomo_scanner/fomo_main.py

from fomo_scanner.fomo_core import fetch_and_process_fomo_data

def check_fomo_signals():
    try:
        result = fetch_and_process_fomo_data()
        if result:
            return {
                "status": True,
                "message": result["alert"],
                "confidence": "medium"
            }
        else:
            return {"status": False}
    except Exception as e:
        print(f"[FOMO Scanner Error] {e}")
        return {"status": False}




