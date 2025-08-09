import os
import asyncio
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    PicklePersistence,
)
from telegram.error import Conflict

# Ініціалізація бота
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
PERSISTENCE_FILE = "bot_data.pickle"

# Створення додатка зі збереженням стану
persistence = PicklePersistence(filepath=PERSISTENCE_FILE)
app = Application.builder().token(TOKEN).persistence(persistence).build()

# Обробник команди /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔄 Бот успішно перезапущений!")

# Обробник помилок
async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE):
    print(f"⚠️ Помилка: {context.error}")

# Основна функція
async def main():
    # Додаємо обробники
    app.add_handler(CommandHandler("start", start))
    app.add_error_handler(error_handler)

    # Запускаємо бота
    try:
        print("🤖 Запуск бота...")
        await app.bot.delete_webhook(drop_pending_updates=True)
        await app.initialize()
        await app.start()
        print("✅ Бот успішно запущений!")
        while True:
            await asyncio.sleep(3600)  # Нескінченний цикл
    except Conflict:
        print("⚠️ Виявлено конфлікт: інший екземпляр бота вже працює")
    except Exception as e:
        print(f"❌ Критична помилка: {e}")
    finally:
        await app.stop()
        await app.shutdown()

if __name__ == "__main__":
    asyncio.run(main())
