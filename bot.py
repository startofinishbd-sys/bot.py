import os
from telegram import Update
from telegram.ext import Application, CommandHandler

BOT_TOKEN = "8826486988:AAFOOfdcrVCgvj532plzOQUXwx40yn3USl0"

async def start(update: Update, context):
    await update.message.reply_text("✅ Bot is alive!")

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("Bot started...")
    app.run_polling()

if __name__ == "__main__":
    main()
