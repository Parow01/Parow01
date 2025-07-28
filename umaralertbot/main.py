from keepalive import keep_alive
from telegram import Bot, Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

import os

BOT_TOKEN = "8092340392:AAHJN8d8mjQgHQeSAEyIYjEu0PesfQf0GH4"
WEBHOOK_URL = "https://parow01.onrender.com"  # ← Matches Render URL

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Welcome to UmarAlertBot! ✅")

def main():
    keep_alive()
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    app.run_webhook(
        listen="0.0.0.0",
        port=8080,
        webhook_url=f"{WEBHOOK_URL}/webhook"
    )

if __name__ == '__main__':
    main()


