import re

def sanitize_text(text: str) -> str:
    """
    Clean and escape unwanted characters from Telegram HTML format.
    """
    if not isinstance(text, str):
        return str(text)
    clean = re.sub(r'[<>]', '', text)
    return clean.strip()
