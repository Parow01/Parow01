from keepalive import keep_alive
from telegram import Bot, Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import logging
import os

# Telegram Bot Token
TOKEN = "8092340392:AAHJN8d8mjQgHQeSAEyIYjEu0PesfQf0GH4"

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Start command handler
def start(update: Update, context: CallbackContext):
    update.message.reply_text("✅ UmarAlertBot is alive and running!")

# Main function
def main():
    keep_alive()  # Start Flask web server for Render

    bot = Bot(token=TOKEN)
    bot.set_webhook(url="https://parow01.onrender.com")  # Webhook URL for Render

    updater = Updater(token=TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

