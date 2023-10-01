from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from states.states import Register
from loader import dp



@dp.message_handler(Command('register'))
async def register(message: types.Message):
    await message.answer("Привіт, давай зареэструємось \nВведи своє ім'я та прізвище")
    await Register.name.set()

@dp.message_handler(state=Register.name)
async def name(message: types.Message, state:FSMContext):
    answer = message.text

    await state.update_data(name=answer)
    await message.answer(f'{answer} в якому ти класі?')
    await Register.clas.set()

@dp.message_handler(state=Register.clas)
async def clas(message: types.Message, state:FSMContext):
    answer = message.text

    await state.update_data(clas=answer)
    name = await state.get_data('name')
    clas = await state.get_data('name')
    await message.answer(f"Реєстрація завершена\n"
                         f"Твоє ім'я {name}\n"
                         f"Ти в {clas} класі")
    await Register.clas.set()
