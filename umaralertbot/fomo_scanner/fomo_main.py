import threading
import time

def fomo_scanner_loop():
    while True:
        try:
            print("🔍 FOMO Scanner is running...")
            time.sleep(30)
        except Exception as e:
            print(f"FOMO Scanner error: {e}")
            time.sleep(10)

def start_fomo_scanner():
    thread = threading.Thread(target=fomo_scanner_loop, daemon=True)
    thread.start()
