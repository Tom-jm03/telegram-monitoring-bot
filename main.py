import telegram, asyncio, os, aiohttp
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters
from functions import get_monitoring_stats
load_dotenv()
Token = os.getenv('Token')
URL = os.getenv('URL')
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context._user_id == 1927247333:
        print("Admin contacted me")

async def monitoring(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context._user_id == 1927247333:
        stats = await get_monitoring_stats()
        await update.message.reply_text(stats)
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