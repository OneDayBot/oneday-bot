import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from cities import CITY_CHANNELS

# Конфігурація
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
PERSISTENCE_FILE = "user_data.pickle"  # Файл для збереження даних

def main():
    # Ініціалізація зі збереженням стану
    persistence = PicklePersistence(filepath=PERSISTENCE_FILE)
    app = Application.builder().token(TOKEN).persistence(persistence).build()
    
    # Реєстрація команд
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("menu", show_menu))
    
    # Запуск
    print("🤖 OneDayBot активовано!")
    app.run_polling()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обробка команди /start"""
    await update.message.reply_text(
        "🇺🇦 Ласкаво просимо до OneDayBot!\n"
        "🇸🇰 Vitajte v OneDayBot!"
    )

async def show_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Показ головного меню"""
    keyboard = [
        [InlineKeyboardButton("🏠 Головне меню", callback_data="main_menu")]
    ]
    await update.message.reply_text(
        "Оберіть опцію:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

if __name__ == "__main__":
    main()
