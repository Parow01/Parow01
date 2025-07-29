# ✅ umaralertbot/confluence_engine/confluence_main.py

import logging
from confluence_engine.confluence_main import ConfluenceSignalEngine

# Dummy signal providers for now
def get_dummy_token_flow_signal():
    return "bullish"

def get_dummy_netflow_signal():
    return "bullish"

def get_dummy_whale_signal():
    return "bearish"

def run_confluence_analysis():
    try:
        engine = ConfluenceSignalEngine()

        token_flow = get_dummy_token_flow_signal()
        netflow = get_dummy_netflow_signal()
        whale = get_dummy_whale_signal()

        result = engine.check_confluence_signal(token_flow, netflow, whale)

        logging.info(f"🔁 [Confluence Engine] Combined signal = {result.upper()}")

        # In future: send_telegram_alert(f"📊 Confluence Signal: {result.upper()}")

    except Exception as e:
        logging.error(f"❌ [Confluence Engine Error] {e}")

def start_confluence_engine(scheduler):
    try:
        scheduler.add_job(
            run_confluence_analysis,
            trigger='interval',
            seconds=90,
            id='confluence_engine_job',
            replace_existing=True
        )
        logging.info("✅ Confluence Engine scheduled successfully.")
    except Exception as e:
        logging.error(f"❌ Failed to start Confluence Engine: {e}")


