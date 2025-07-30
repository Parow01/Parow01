def format_alert(title: str, data: dict) -> str:
    """
    Format alert messages into a clean structure for Telegram delivery.
    """
    lines = [f"🚨 <b>{title}</b> 🚨", ""]
    for key, value in data.items():
        lines.append(f"<b>{key}:</b> {value}")
    return "\n".join(lines)

