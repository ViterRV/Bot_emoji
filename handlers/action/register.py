from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from states.states import Register
from loader import dp
from utils.db_api.db_registration import create_profile_registration


@dp.message_handler(text='/register')
async def register(message: types.Message):
    await message.answer("Введи ім'я")
    await Register.first_name.set()

@dp.message_handler(state=Register.first_name)
async def add_first_name(message: types.Message, state:FSMContext):
    async with state.proxy() as register:
        register['first_name'] = message.text
    await message.answer(f'{message.text}, введи прізвище')
    await Register.last_name.set()

@dp.message_handler(state=Register.last_name)
async def add_first_name(message: types.Message, state: FSMContext):
    async with state.proxy() as register:
        register['last_name'] = message.text
    id = message.from_user.id
    await create_profile_registration(state,id)
    await message.answer("Реєстрація завершена")
    await state.finish()
