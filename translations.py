# -*- coding: utf-8 -*-
"""
Модуль для перекладів та текстових шаблонів
"""

# Словник перекладів для інтерфейсу
UI_TRANSLATIONS = {
    "UA": {
        "start": "🇺🇦 Ласкаво просимо до OneDayVS!\nОберіть мову:",
        "city_select": "🏙 Оберіть місто:",
        "description": "📝 Введіть опис завдання:",
        "error": "❌ Помилка. Спробуйте ще раз."
    },
    "SK": {
        "start": "🇸🇰 Vitajte v OneDayVS!\nVyberte jazyk:",
        "city_select": "🏙 Vyberte mesto:",
        "description": "📝 Zadajte popis úlohy:",
        "error": "❌ Chyba. Skúste znova."
    }
}

# Шаблони оголошень
POST_TEMPLATES = {
    "UA": {
        "header": "🔔 <b>Нова заявка</b>\n\n",
        "city": "🏙 <b>Місто:</b> {city}\n",
        "payment": "💰 <b>Оплата:</b> {payment}€"
    },
    "SK": {
        "header": "🔔 <b>Nová požiadavka</b>\n\n",
        "city": "🏙 <b>Mesto:</b> {city}\n",
        "payment": "💰 <b>Platba:</b> {payment}€"
    }
}

def get_translation(key: str, language: str = "UA") -> str:
    """Повертає переклад для вказаного ключа"""
    return UI_TRANSLATIONS.get(language, {}).get(key, key)

def format_post(data: dict, language: str = "UA") -> str:
    """Форматує оголошення згідно з обраною мовою"""
    template = POST_TEMPLATES.get(language, {})
    return (
        template.get("header", "") +
        template.get("city", "").format(city=data.get("city")) +
        template.get("description", "").format(description=data.get("description")) +
        template.get("payment", "").format(payment=data.get("payment"))
    )

# Приклад використання:
if __name__ == "__main__":
    print(get_translation("start", "UA"))
    test_data = {"city": "Bratislava", "description": "Потрібен вантажник", "payment": "50"}
    print(format_post(test_data, "UA"))
