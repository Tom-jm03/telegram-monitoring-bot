import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters
from functions import get_monitoring_stats
from datetime import datetime, timedelta
load_dotenv()
Token = os.getenv('Token')
URL = os.getenv('URL')
user = os.getenv('user')
password = os.getenv('password')
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context._user_id == 1927247333:
        print("Admin contacted me")

async def monitoring(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context._user_id == 1927247333:
        stats = await get_monitoring_stats(URL, user, password)
        dt = datetime.fromtimestamp(stats[7])
        await update.message.reply_text(f"CPU-Temperatur: {stats[0]}°C \nRAM {stats[1]}GB gesamt, {stats[2]}GB belegt, {stats[3]}GB frei \nLoad: {stats[4]}, {stats[5]}, {stats[6]}\n\nZeitpunkt: {dt.strftime('%H:%M:%S %d.%m.%Y')}")

    else:
        await update.message.reply_text("You are not allowed to use this command")

    
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(update.message.text)

if __name__ == '__main__':
    print("Starting...")
    application = ApplicationBuilder().token(Token).build()
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
    start_handler = CommandHandler('start', start)
    monitoring_handler = CommandHandler('monitoring', monitoring)
    application.add_handler(start_handler)
    application.add_handler(echo_handler)
    application.add_handler(monitoring_handler)
    application.run_polling()
