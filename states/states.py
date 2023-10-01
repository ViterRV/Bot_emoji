from aiogram.dispatcher.filters.state import StatesGroup, State


class ProfileStates(StatesGroup):
    id_update = State()
    id_delete = State()
    user_name = State()
    emoji = State()
    emoji1 = State()
    value = State()
    what_heppend = State()
    editing = State()

class Register(StatesGroup):
    name = State()
    clas = State()

