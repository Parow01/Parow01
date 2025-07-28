from keepalive import keep_alive
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os
import threading
import pytz  # ✅ Required for APScheduler timezones

from alert_engine.alert_main import start_alert_engine
from fomo_scanner.fomo_main import start_fomo_scanner
from whale_engine.whale_main import start_whale_engine
from whale_screener.screener_main import start_whale_screener  # ✅ Added this

BOT_TOKEN = os.environ.get("BOT_TOKEN") or "8092340392:AAHJN8d8mjQgHQeSAEyIYjEu0PesfQf0GH4"
WEBHOOK_URL = "https://parow01.onrender.com"

# ✅ Telegram /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ UmarAlertBot is live and running!")

# ✅ Launch each background engine in its own thread
def run_background_jobs():
    threading.Thread(target=start_alert_engine, daemon=True).start()
    threading.Thread(target=start_fomo_scanner, daemon=True).start()
    threading.Thread(target=start_whale_engine, daemon=True).start()
    threading.Thread(target=start_whale_screener, daemon=True).start()

# ✅ Telegram bot main webhook app
async def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))

    run_background_jobs()

    await app.bot.set_webhook(url=WEBHOOK_URL)
    await app.run_webhook(
        listen="0.0.0.0",
        port=8080,
        webhook_url=WEBHOOK_URL,
    )

# ✅ Entry point
if __name__ == "__main__":
    keep_alive()

    import asyncio
    loop = asyncio.get_event_loop()
    loop.create_task(main())
    loop.run_forever()




