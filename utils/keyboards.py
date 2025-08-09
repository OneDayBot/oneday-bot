from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def city_keyboard():
    """Клавіатура для вибору міста"""
    buttons = [
        [InlineKeyboardButton("Bratislava", callback_data="city_bratislava")],
        [InlineKeyboardButton("Košice", callback_data="city_kosice")]
    ]
    return InlineKeyboardMarkup(buttons)
