import os
from datetime import datetime

# Directory for logs
LOG_DIR = "logs"
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

def log_event(event: str, filename: str = "bot.log"):
    """Writes an event to the specified log file"""
    timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"[{timestamp}] {event}\n"
    try:
        with open(os.path.join(LOG_DIR, filename), "a") as f:
            f.write(entry)
    except Exception as e:
        print(f"[LOGGING ERROR] {e}")

def log_alert(message: str):
    log_event(message, filename="alerts.log")

def log_ram(memory_status: str):
    log_event(memory_status, filename="ram.log")
