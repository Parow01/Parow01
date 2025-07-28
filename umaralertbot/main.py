import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from keepalive import keep_alive
from apscheduler.schedulers.background import BackgroundScheduler
from whale_engine.whale_main import start_whale_engine
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
WEBHOOK_URL = "https://parow01.onrender.com/webhook"

app = ApplicationBuilder().token(BOT_TOKEN).build()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Welcome! Parownewbot is live and responding.")

app.add_handler(CommandHandler("start", start))

scheduler = BackgroundScheduler()
start_whale_engine(scheduler)
scheduler.start()

keep_alive()

app.run_webhook(
    listen="0.0.0.0",
    port=8080,
    webhook_url=WEBHOOK_URL,
    allowed_updates=Update.ALL_TYPES
)




