from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

bosh_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🎁 Купить"),
            KeyboardButton(text="📱 Профиль"),
            KeyboardButton(text="ℹ️ FAQ"),
        ],   
        [
            KeyboardButton(text="📕 Поддержка"),
            KeyboardButton(text="▶️ Информация")
        ],
    ],
    resize_keyboard=True
)