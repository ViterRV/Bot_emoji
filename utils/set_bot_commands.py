from aiogram import types
from handlers.action import start
async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand('start', 'Головне меню'),
        types.BotCommand('help','Допомога'),
        types.BotCommand('register', 'Реєстрація')
    ])