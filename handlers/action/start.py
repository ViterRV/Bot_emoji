from aiogram import types
from loader import dp
from keyboards.menu_keyboards import rkm
from utils.db_api.db_registration import read_db_registration


@dp.message_handler(text='/start')
async def start(message: types.Message):
    data = await read_db_registration(user_id=message.from_user.id)
    if data:
        await message.answer('Menu', reply_markup=rkm)

    else:
        await message.answer(text='Ти ще не зареєстрований, натисни - /register')





