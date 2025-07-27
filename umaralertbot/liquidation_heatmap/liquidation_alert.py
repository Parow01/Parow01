import random

def check_liquidation_clusters() -> dict | None:
    """
    Simulates checking for liquidation events.
    Replace this with CoinGlass or other data in real implementation.
    """
    liquidation_volume = random.randint(10, 120)  # Simulate $M

    if liquidation_volume >= 50:
        return {
            "type": "liquidation",
            "alert": f"💥 ${liquidation_volume}M Liquidations detected in 5min!\nWatch for volatility surge.",
            "volume_m": liquidation_volume
        }

    return None
