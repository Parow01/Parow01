import re

def sanitize_text(text: str) -> str:
    """
    Clean and escape unwanted characters from Telegram HTML format.
    """
    if not isinstance(text, str):
        text = str(text)
    text = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    return text.strip()

