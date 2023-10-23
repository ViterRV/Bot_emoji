from aiogram import executor
#from handlers import dp
from loader import dp
from utils.db_api.db_emoji import db_start
from utils.db_api.db_registration import register_db
from utils.notify_admin import on_startup_notify
from utils.set_bot_commands import set_default_commands


async def on_startup(dp):
    await on_startup_notify(dp)
    await set_default_commands(dp)
    await db_start()
    await register_db()
    print("Bot starts")

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup )