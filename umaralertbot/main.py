# parownewbot/main.py

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import logging

BOT_TOKEN = "8092340392:AAHJN8d8mjQgHQeSAEyIYjEu0PesfQf0GH4"

# ✅ Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

# ✅ Define /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Welcome! Parownewbot is live and responding.")

# ✅ Define /help command (optional)
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("ℹ️ Available commands:\n/start - Launch bot\n/help - Show this message")

# ✅ Start the bot
if __name__ == "__main__":
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    # Add command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))

    # Run webhook
    application.run_webhook(
        listen="0.0.0.0",
        port=8080,
        webhook_url="https://parow01.onrender.com/webhook"
    )





