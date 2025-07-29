# alert_formatter.py

def format_alert_message(alert: dict) -> str:
    """
    Format the alert dict into a clean Telegram-friendly message.
    """
    alert_type = alert.get("type", "Unknown")
    body = alert.get("alert", "No alert message provided.")
    confidence = alert.get("confidence", "")
    direction = alert.get("direction", "")
    
    message = f"🚨 <b>{alert_type.upper()}</b>\n\n{body}"
    
    if confidence:
        message += f"\n\n🧠 Confidence: <b>{confidence.capitalize()}</b>"
    if direction:
        message += f"\n📊 Direction: <b>{direction.capitalize()}</b>"

    return message
