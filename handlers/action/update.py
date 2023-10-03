from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from keyboards.emoji_menu import inline_kb
from loader import dp
from states.states import ProfileStates
from utils.db_api.db_emoji import read_db, check_record


@dp.message_handler(Text(equals="Редагувати запис 📝"))
async def edit_records(message: types.Message):
    if message.from_user.id == 346422904:
        data = await read_db()
        await message.answer(text=f"<b>Список записів:</b>\n\n{data}\n\nВведіть номер ID запису для редагування",
                             parse_mode=types.ParseMode.HTML)
    else:
        data = await read_db(user_id=message.from_user.id)
        await message.answer(text=f"<b>Список записів:</b>\n\n{data}\n\nВведіть номер ID запису для редагування",
                             parse_mode=types.ParseMode.HTML)

    await ProfileStates.id_update.set()

@dp.message_handler(state=ProfileStates.id_update)
async def number_id_for_update(message,state:FSMContext):
    try:
        id = int(message.text)
        if id > 0:
            async with state.proxy() as data:
                data['id_update'] = id
            if message.from_user.id == 346422904:
                data = await check_record(id=id)
                if data == True:
                    await message.answer('Виберіть емоцію', reply_markup=inline_kb)
                    print(message.text)
                    await ProfileStates.emoji.set()
                else:
                    await message.answer(f'Запису № {id} не існує')
            else:
                data = await check_record(id=id,user_id=message.from_user.id)
                if data == True:
                    await message.answer('Виберіть емоцію', reply_markup=inline_kb)
                    print(message.text)
                    await ProfileStates.emoji.set()
                else:
                    await message.answer(f'Запису № {id} не існує')
        else:
            await message.reply('Введіть коректне число')
    except ValueError:
        await message.answer('Введіть коректне число')