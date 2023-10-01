from aiogram import executor
#from handlers import dp
from loader import dp
from utils.notify_admin import on_startup_notify
from utils.set_bot_commands import set_default_commands


async def on_startup(dp):
    await on_startup_notify(dp)
    await set_default_commands(dp)
    print("Bot starts")

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup )