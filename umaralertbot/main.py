import logging
import os
from dotenv import load_dotenv
from flask import Flask, request
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
)
from apscheduler.schedulers.background import BackgroundScheduler

from keepalive import keep_alive
from whale_engine.whale_main import start_whale_engine

# Load environment variables
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")

# Set up logging
logging.basicConfig(level=logging.INFO)

# Flask app
app = Flask(__name__)

# Telegram command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Hello! Parownewbot is live and ready!")

# Create scheduler
scheduler = BackgroundScheduler()
scheduler.start()

# Telegram app
telegram_app = ApplicationBuilder().token(BOT_TOKEN).build()
telegram_app.add_handler(CommandHandler("start", start))

# Start whale alert engine
start_whale_engine(scheduler)

# Flask route for root
@app.route("/", methods=["GET"])
def home():
    return "✅ Parownewbot is live!"

# Flask route for Telegram webhook
@app.route("/webhook", methods=["POST"])
def webhook():
    if request.method == "POST":
        update = Update.de_json(request.get_json(force=True), telegram_app.bot)
        telegram_app.update_queue.put(update)
        return "OK", 200

# Run everything
if __name__ == "__main__":
    keep_alive(app)
    telegram_app.run_webhook(
        listen="0.0.0.0",
        port=8080,
        webhook_url=WEBHOOK_URL + "/webhook"
    )



