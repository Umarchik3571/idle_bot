from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup

from aiogram import types


async def mi_line_btn():
    btn=types.InlineKeyboardMarkup(row_width=1)
    btn.add(
        types.InlineKeyboardButton("Пробив по номеру",callback_data="n1"),
        types.InlineKeyboardButton("МВД",callback_data="n2"),
        types.InlineKeyboardButton("ФНС",callback_data="n3"),
        types.InlineKeyboardButton("ПФР",callback_data="n4"),
        types.InlineKeyboardButton("Мини-досъе(автодача)",callback_data="n5"),
        types.InlineKeyboardButton("Верефикация Готовые кошельки",callback_data="n6"),
        types.InlineKeyboardButton("Мобильные операторы",callback_data="n7"),
        types.InlineKeyboardButton("Флуд и рассылка",callback_data="n8"),
        types.InlineKeyboardButton("Пробив КИ",callback_data="n9"),
        types.InlineKeyboardButton("Сертефикат Ковид",callback_data="n10"),
        types.InlineKeyboardButton("Документы",callback_data="n11"),
    )
    return btn

async def mi_liner_btn():
    btn=types.InlineKeyboardMarkup(row_width=1)
    btn.add(
        types.InlineKeyboardButton("Пополнить",callback_data="n1"),
        types.InlineKeyboardButton("Мои заказы",callback_data="n2"),
    )
    return btn