from aiogram import types
from loader import dp
from keyboards.menu_keyboards import rkm

@dp.message_handler(text='/start')
async def start(message: types.Message):
    await message.answer('Menu',
                        reply_markup=rkm)

