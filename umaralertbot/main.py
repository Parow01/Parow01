import logging
from telegram.ext import Updater, CommandHandler
from keepalive import keep_alive
import os

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Load token
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# Define a simple command handler
def start(update, context):
    update.message.reply_text("🚀 UmarAlertBot is alive and monitoring!")

def main():
    keep_alive()

    # Set up the updater and dispatcher
    updater = Updater(token=TOKEN, use_context=True)
    dp = updater.dispatcher

    # Add command handlers
    dp.add_handler(CommandHandler("start", start))

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

