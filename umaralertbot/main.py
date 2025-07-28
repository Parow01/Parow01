from keepalive import keep_alive
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os
import threading

# ✅ Updated bot username (Parownewbot) and token (you provided)
BOT_TOKEN = os.getenv("BOT_TOKEN") or "8092340392:AAHJN8d8mjQgHQeSAEyIYjEu0PesfQf0GH4"
WEBHOOK_URL = "https://parow01.onrender.com/webhook"  # ✅ Important: include /webhook

# ✅ Import background engines
from alert_engine.alert_main import start_alert_engine
from fomo_scanner.fomo_main import start_fomo_scanner
from whale_engine.whale_main import start_whale_engine

# ✅ /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Parownewbot is live and running!")

# ✅ Background tasks
def run_background_jobs():
    threading.Thread(target=start_alert_engine, daemon=True).start()
    threading.Thread(target=start_fomo_scanner, daemon=True).start()
    threading.Thread(target=start_whale_engine, daemon=True).start()
    # Add more threads as needed

async def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))

    run_background_jobs()

    await app.bot.set_webhook(url=WEBHOOK_URL)  # ✅ Sets the correct /webhook URL

    await app.run_webhook(
        listen="0.0.0.0",
        port=8080,
        webhook_url=WEBHOOK_URL,
        path="/webhook",  # ✅ Must match the webhook path
    )

if __name__ == "__main__":
    keep_alive()
    import asyncio
    asyncio.run(main())





