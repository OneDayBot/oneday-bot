import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from translations import get_text, create_post

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
app = Application.builder().token(TOKEN).build()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(get_text("start", "UA"))

async def publish(update: Update, context: ContextTypes.DEFAULT_TYPE):
    test_data = {"city": "Bratislava", "description": "Test", "payment": "50"}
    await update.message.reply_text(create_post(test_data, "UA"), parse_mode="HTML")

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("publish", publish))

if __name__ == "__main__":
    print("🤖 Бот запущено!")
    app.run_polling()
