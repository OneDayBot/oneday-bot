# Простий словник для базового перекладу
TRANSLATIONS = {
    "UA": {
        "city": "Місто",
        "description": "Опис"
    },
    "SK": {
        "city": "Mesto",
        "description": "Popis"
    }
}

def translate(text: str, lang: str) -> str:
    return TRANSLATIONS.get(lang, {}).get(text, text)
