from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from telegram import Update
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Бот працює!")

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_text = """
Доступні команди:
/start - Перевірити, чи бот працює
/help - Отримати довідку
"""
    await update.message.reply_text(help_text)

async def _post_init(app):
    # гарантуємо, що polling не конфліктує з можливим webhook
    await app.bot.delete_webhook(drop_pending_updates=True)

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).post_init(_post_init).build()
    
    # Додаємо обробники команд
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help))
    
    app.run_polling(allowed_updates=Update.ALL_TYPES, drop_pending_updates=True)

if __name__ == "__main__":
    main()
