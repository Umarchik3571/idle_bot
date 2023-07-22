import logging

from aiogram import Bot,Dispatcher, executor, types
from btn import bosh_menu
from inline_btn import mi_line_btn, mi_liner_btn


BOT_TOKEN = '5623693354:AAHtdOHmTqQd43d4XEZHWcGF9geWr6Pdinw'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN, parse_mode="html")
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.answer(text="""
🙋‍♀️Привет дорогой друг!
Меня зовут Пробив Бот""",reply_markup=bosh_menu)

@dp.message_handler(text=['🎁 Купить'])
async def send_welcomee(message: types.Message):
    await message.answer("🎁 Выберите нужную вам услугу:",reply_markup=await mi_line_btn())


@dp.message_handler(text='📱 Профиль')
async def send_welcomee(message: types.Message):
    await message.answer(f"""
    📱 Ваш профиль:
➖➖➖➖➖➖➖➖➖➖➖➖➖
🔑 Мой ID: {message.from_user.id}
👤 Логин: @{message.from_user.username}
🕜 Регистрация: 20/05/2023 09:55:32
➖➖➖➖➖➖➖➖➖➖➖➖➖
💳 Баланс: 0.0 р
👥Вы пригласили: 0 человек
🔗Ссылка для приглашения: https://t.me/Probiv2bot?start=1401426""",reply_markup=await mi_liner_btn())
    
@dp.message_handler(text='ℹ️ FAQ')
async def send_welcomeee(message: types.Message):
    await message.answer("""
    Данный бот, поможет вам найти кого угодно.
Наши плюсы:
➕Удобное использование
➕Автоматическая оплата
➕Вашим заказом занимаются профессионалы
➕Прямая связь с саппортом
➕Выдача заказа в сроки

Помощь/предложить свои услуги - @kaban_service""")

@dp.message_handler(text='▶️ Информация')
async def send_welcomeeee(message: types.Message):
    await message.answer("""
    Работаем быстро и качественно ✅

Помощь/предложить свои услуги - @kaban_service""")

@dp.message_handler(text='📕 Поддержка')
async def send_welcomeeee(message: types.Message):
    await message.answer("""📕 Писать сюда ➡️ @kaban_service""")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)