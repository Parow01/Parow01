import asyncio
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
from whale_engine.whale_main import start_whale_engine
from whale_screener.screener_main import start_whale_screener
from fomo_scanner.fomo_main import start_fomo_scanner
import threading

BOT_TOKEN = os.getenv("BOT_TOKEN", "8092340392:AAHJN8d8mjQgHQeSAEyIYjEu0PesfQf0GH4")
WEBHOOK_URL = "https://parow01.onrender.com/webhook"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Parownewbot is online!")

def run_background_tasks():
    threading.Thread(target=start_whale_engine).start()
    threading.Thread(target=start_whale_screener).start()
    threading.Thread(target=start_fomo_scanner).start()

async def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))

    run_background_tasks()

    await app.run_webhook(
        listen="0.0.0.0",
        port=8080,
        webhook_url=WEBHOOK_URL,
        allowed_updates=Update.ALL_TYPES
    )

if __name__ == "__main__":
    asyncio.run(main())




