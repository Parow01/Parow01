import os
import logging
from flask import Flask, request
import telegram
from telegram.ext import Dispatcher, CommandHandler, MessageHandler, Filters
from config import TELEGRAM_TOKEN, WEBHOOK_URL

# Initialize Flask app
app = Flask(__name__)

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Initialize Telegram Bot
bot = telegram.Bot(token=TELEGRAM_TOKEN)

# Set up dispatcher
dispatcher = Dispatcher(bot, None, use_context=True)

# Simple command handler (you can expand later)
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="👋 Hello! UmarAlertBot is active.")

dispatcher.add_handler(CommandHandler("start", start))

@app.route(f"/{TELEGRAM_TOKEN}", methods=["POST"])
def webhook():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    dispatcher.process_update(update)
    return "OK", 200

@app.route("/")
def home():
    return "🤖 UmarAlertBot is Live!", 200

if __name__ == "__main__":
    # Set webhook once when the app starts
    bot.set_webhook(url=f"{WEBHOOK_URL}/{TELEGRAM_TOKEN}")
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
