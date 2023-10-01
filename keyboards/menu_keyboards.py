from aiogram.types import ReplyKeyboardMarkup,\
    KeyboardButton

rkm = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton(text="Додати запис ✍️"),
                                KeyboardButton(text="Переглянути записи 👀")).add(
                                KeyboardButton(text="Редагувати запис 📝"),
                                KeyboardButton(text="Видалити запис ✖️"))