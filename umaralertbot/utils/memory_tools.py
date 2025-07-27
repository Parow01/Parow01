import psutil
import os
import gc

# RAM thresholds (in MB)
MAX_RAM_MB = 450
MIN_RAM_MB = 300
CLEAR_RAM_MB = 400

def get_memory_usage_mb():
    """Returns current RAM usage in MB"""
    process = psutil.Process(os.getpid())
    mem = process.memory_info().rss / (1024 * 1024)  # Convert to MB
    return round(mem, 2)

def is_ram_high():
    """Returns True if RAM is above the pause threshold"""
    return get_memory_usage_mb() > MAX_RAM_MB

def is_ram_safe():
    """Returns True if RAM is low enough to resume"""
    return get_memory_usage_mb() < MIN_RAM_MB

def clear_memory_if_needed():
    """Triggers manual garbage collection if RAM is above soft threshold"""
    if get_memory_usage_mb() > CLEAR_RAM_MB:
        gc.collect()
        return True
    return False

def get_memory_health():
    """Returns status text for /status command"""
    mem = get_memory_usage_mb()
    if mem > MAX_RAM_MB:
        return f"❌ High ({mem}MB) — Alerts Paused"
    elif mem > CLEAR_RAM_MB:
        return f"⚠️ Warning ({mem}MB) — Auto Cleanup Triggered"
    elif mem > MIN_RAM_MB:
        return f"🟡 Moderate ({mem}MB)"
    else:
        return f"✅ Healthy ({mem}MB)"
