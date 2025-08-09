# -*- coding: utf-8 -*-
UI_TRANSLATIONS = {
    "UA": {
        "start": "🇺🇦 Ласкаво просимо!\nОберіть мову:",
        "city": "🏙 Місто:",
        "payment": "💰 Оплата:",
        "error": "❌ Помилка"
    },
    "SK": {
        "start": "🇸🇰 Vitajte!\nVyberte jazyk:",
        "city": "🏙 Mesto:",
        "payment": "💰 Platba:",
        "error": "❌ Chyba"
    }
}

POST_TEMPLATES = {
    "UA": {
        "header": "🔔 <b>Оголошення</b>\n",
        "full_post": "🏙 <b>Місто:</b> {city}\n📝 <b>Опис:</b> {description}\n💰 <b>Оплата:</b> {payment}€"
    },
    "SK": {
        "header": "🔔 <b>Inzerát</b>\n",
        "full_post": "🏙 <b>Mesto:</b> {city}\n📝 <b>Popis:</b> {description}\n💰 <b>Platba:</b> {payment}€"
    }
}

def get_text(key: str, lang: str) -> str:
    return UI_TRANSLATIONS.get(lang, {}).get(key, key)

def create_post(data: dict, lang: str) -> str:
    return POST_TEMPLATES[lang]["header"] + POST_TEMPLATES[lang]["full_post"].format(**data)
