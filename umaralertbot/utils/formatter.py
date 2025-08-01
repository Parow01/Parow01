# utils/formatter.py

from utils.sanitizer import sanitize_text

def format_alert(title: str, data: dict) -> str:
    """
    Format alert messages into a Telegram-ready HTML string.
    """
    lines = [f"🚨 <b>{sanitize_text(title)}</b> 🚨", ""]
    for key, value in data.items():
        key_clean = sanitize_text(key)
        value_clean = sanitize_text(value)
        lines.append(f"<b>{key_clean}:</b> {value_clean}")
    return "\n".join(lines)


