from os import getenv

class Config:
    TOKEN = getenv("TELEGRAM_BOT_TOKEN")
    ADMIN_ID = int(getenv("ADMIN_ID", 924805332))
    MAIN_CHANNEL = getenv("MAIN_CHANNEL", "@OneDaySK")
    SPAM_KEYWORDS = ["spam", "scam", "реклама"]
