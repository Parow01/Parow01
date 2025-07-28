# umaralertbot/message_router/message_router_main.py

from alert_manager import alert_manager_main
from utils.chat_ids import CHAT_IDS

def route_message(alert_type, message):
    """
    Routes messages based on alert type to specific Telegram chat IDs.
    """
    if alert_type == "whale":
        targets = CHAT_IDS["whale"]
    elif alert_type == "fomo":
        targets = CHAT_IDS["fomo"]
    elif alert_type == "liquidation":
        targets = CHAT_IDS["liquidation"]
    else:
        targets = CHAT_IDS["general"]

    for chat_id in targets:
        alert_manager_main.send_telegram_alert(chat_id, message)
