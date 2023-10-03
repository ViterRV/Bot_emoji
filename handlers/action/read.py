from aiogram import types
from aiogram.dispatcher.filters import Text
from loader import dp
from utils.db_api.db_emoji import read_db


@dp.message_handler(Text(equals="Переглянути записи 👀"))
async def read(message: types.Message):
    if message.from_user.id == 346422904:
        data = await read_db()
        await message.answer(data)
    else:
        data = await read_db(user_id= message.from_user.id)
        await message.answer(data)