from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp
from states.states import ProfileStates
from keyboards.emoji_menu import *
from datetime import datetime

@dp.message_handler(text="Додати запис ✍️")
async def start(message: types.Message):
    await message.answer("Привіт! Як справи? Обери свій стан!",
                        reply_markup=inline_kb)

    await ProfileStates.emoji.set()  # установлюмо стан емоції


@dp.callback_query_handler(state=ProfileStates.emoji)
async def callback_emoji(callback: types.CallbackQuery, state:FSMContext):
    async with state.proxy() as data:
        data['emoji'] = callback.data
    if data['emoji'] == "Радість":
        await callback.message.reply(text='зробіть вибір', reply_markup=keyboard(key_happy))
    elif data['emoji'] == "Сила":
        await callback.message.reply(text='зробіть вибір', reply_markup=keyboard(key_force))
    elif data['emoji'] == "Спокій":
        await callback.message.reply(text='зробіть вибір', reply_markup=keyboard(key_calm))
    elif data['emoji'] == "Смуток":
        await callback.message.reply(text='зробіть вибір', reply_markup=keyboard(key_sadness))
    elif data['emoji'] == "Навіженість":
        await callback.message.reply(text='зробіть вибір', reply_markup=keyboard(key_fury))
    elif data['emoji'] == "Страх":
        await callback.message.reply(text='зробіть вибір', reply_markup=keyboard(key_fear))
    await ProfileStates.next()


@dp.callback_query_handler(state=ProfileStates.emoji1)
async def emoji1(callback: types.CallbackQuery, state:FSMContext):
    async with state.proxy() as data:
        data['emoji1'] = callback.data
    await callback.message.reply('Виберіть рівень емоції від 0 до 10')
    await ProfileStates.next()


@dp.message_handler(state=ProfileStates.value)
async def get_emotion_level(message: types.Message, state: FSMContext):
    try:
        level = int(message.text)
        if 0 <= level <= 10:
            async with state.proxy() as data:
                data['value'] = level
            await message.reply('Що спровокувало?')
            await ProfileStates.next()
        else:
            await message.answer('Введіть рівень емоції від 0 до 10')
    except ValueError:
        await message.answer('Введіть коректне число від 0 до 10')

@dp.message_handler(state=ProfileStates.value)
async def value_emoji(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['value'] = message.text

    await message.reply('Що спровокувало?')
    await ProfileStates.next()

@dp.message_handler(state=ProfileStates.what_heppend)
async def what_heppend(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['what_heppend'] = message.text
        await message.answer('Запис додано')
        await state.finish()
