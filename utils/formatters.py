def format_post_ua(user_data: dict) -> str:
    """Форматування оголошення українською"""
    return f"""
    🏙 Місто: {user_data['city']}
    📝 Опис: {user_data['description']}
    """

def format_post_sk(user_data: dict) -> str:
    """Форматування словацькою (або переклад)"""
    # Тут можна додати переклад через googletrans
    return "..."
