def start_alert_engine():
    print("🚨 Alert engine started.")

import requests
import os

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")  # Set in config.py

def send_alert(alert: dict) -> bool:
    """
    Sends a signal alert to Telegram.
    """
    if not alert:
        return False

    direction_emoji = "🟢" if alert["direction"] == "bullish" else "🔴"
    strength_emoji = {
        "high": "🔥",
        "medium": "⚠️",
    }.get(alert.get("strength", "low"), "❔")

    message = f"{strength_emoji} *{alert['direction'].upper()} SIGNAL*\n{direction_emoji} Confidence: `{alert['strength']}`\n\n"

    for s in alert["alerts"]:
        message += f"• {s['alert']}\n"

    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message,
        "parse_mode": "Markdown",
        "disable_notification": True
    }

    try:
        response = requests.post(
            f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage",
            data=payload,
            timeout=10
        )
        return response.status_code == 200
    except Exception as e:
        print("Alert Error:", e)
        return False
