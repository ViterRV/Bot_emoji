from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from loader import dp
from states.states import ProfileStates
from utils.db_api.db_emoji import read_db, check_record, delete_profile


@dp.message_handler(Text(equals="Видалити запис ✖️"))
async def delete(message: types.Message):
    if message.from_user.id == 346422904:
        data = await read_db()
        await message.answer(text=f"<b>Список записів:</b>\n\n{data}\n\n<b>Введіть номер ID запису для видалення</b>",
                             parse_mode=types.ParseMode.HTML)
    else:
        data = await read_db(user_id=message.from_user.id)
        await message.answer(text=f"<b>Список записів:</b>\n\n{data}\n\n<b>Введіть номер ID запису для видалення</b>",
                             parse_mode=types.ParseMode.HTML)

    await ProfileStates.id_delete.set()
@dp.message_handler(state=ProfileStates.id_delete)
async def number_id_for_delete(message,state:FSMContext):
    try:
        id = int(message.text)
        if id > 0:
            async with state.proxy() as data:
                data['id_delete'] = id
            if message.from_user.id == 346422904:
                data = await check_record(id=id)
                if data == True:
                    await delete_profile(id)
                    await message.answer(f'<b>Запис № {id} видалено</b>',parse_mode=types.ParseMode.HTML)
                else:
                    await message.answer(f'<b>Запису № {id} не існує</b>',parse_mode=types.ParseMode.HTML)
            else:
                data = await check_record(id=id,user_id=message.from_user.id)
                if data == True:
                    await delete_profile(id)
                    await message.answer(f'<b>Запис № {id} видалено</b>',parse_mode=types.ParseMode.HTML)
                else:
                    await message.answer(f'<b>Запису № {id} не існує</b>',parse_mode=types.ParseMode.HTML)
        else:
            await message.reply('Введіть коректне число')
    except ValueError:
        await message.answer('Введіть коректне число')
    await state.finish()