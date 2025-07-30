import requests
import os
import logging
from dotenv import load_dotenv

load_dotenv()

SANTIMENT_API_KEY = os.getenv("SANTIMENT_API_KEY")

def fetch_whale_sentiment():
    try:
        url = "https://api.santiment.net/graphql"
        query = """
        {
            sentiment(
                slug: "bitcoin"
                from: "now-1h"
                to: "now"
                interval: "1h"
            ) {
                positive
                negative
            }
        }
        """
        headers = {
            "Authorization": f"Apikey {SANTIMENT_API_KEY}",
            "Content-Type": "application/json"
        }
        response = requests.post(url, json={"query": query}, headers=headers)
        data = response.json()

        if "data" in data and "sentiment" in data["data"]:
            pos = data["data"]["sentiment"][0]["positive"]
            neg = data["data"]["sentiment"][0]["negative"]

            if pos > 0.8 and neg < 0.2:
                return {
                    "type": "sentiment_alert",
                    "confidence": "high",
                    "source": "Santiment",
                    "symbol": "BTC",
                    "message": f"🧠 **Whale Sentiment Spike Detected!**\n\n> Positive sentiment: `{pos}`\n> Negative sentiment: `{neg}`\n\nLarge wallets show bullish confidence.",
                }
            elif neg > 0.8 and pos < 0.2:
                return {
                    "type": "sentiment_alert",
                    "confidence": "high",
                    "source": "Santiment",
                    "symbol": "BTC",
                    "message": f"⚠️ **Bearish Whale Sentiment Spike**\n\n> Positive sentiment: `{pos}`\n> Negative sentiment: `{neg}`\n\nSmart money may be anticipating downside.",
                }

        return None

    except Exception as e:
        logging.error(f"[Sentiment API Error] {e}")
        return None

