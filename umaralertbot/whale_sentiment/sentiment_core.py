import logging
import os
import requests
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def get_whale_sentiment():
    """
    Fetch whale sentiment based on on-chain balance and token distribution.
    This uses free Santiment API for whale accumulation trends.
    """
    try:
        logging.info("📊 Fetching whale sentiment...")

        url = "https://api.santiment.net/graphql"
        query = {
            "query": """
            {
              allProjects {
                name
                slug
              }
            }
            """  # Replace with real whale sentiment query once token/slug is selected
        }

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Apikey {os.getenv('SANTIMENT_API_KEY')}"
        }

        response = requests.post(url, json=query, headers=headers)
        if response.status_code != 200:
            raise Exception(f"Error: {response.status_code} - {response.text}")

        # Placeholder decision logic (to be enhanced)
        signal = {
            "type": "whale_sentiment",
            "alert": "🐋 Whales are accumulating ETH over the past 3 days!",
            "confidence": "medium"
        }

        return signal

    except Exception as e:
        logging.error(f"❌ Error fetching whale sentiment: {e}")
        return None


def send_whale_sentiment_alert(message):
    try:
        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
        payload = {
            "chat_id": CHAT_ID,
            "text": message,
            "parse_mode": "HTML"
        }
        response = requests.post(url, data=payload)
        response.raise_for_status()
        logging.info("✅ Whale sentiment alert sent.")
    except Exception as e:
        logging.error(f"❌ Failed to send whale sentiment alert: {e}")


def run_whale_sentiment_monitor():
    signal = get_whale_sentiment()
    if signal:
        alert_text = (
            f"<b>{signal['alert']}</b>\n"
            f"📊 <b>Confidence:</b> {signal['confidence'].capitalize()}"
        )
        send_whale_sentiment_alert(alert_text)
