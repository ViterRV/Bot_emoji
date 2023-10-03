import asyncio
import os
#import logging
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types
from handlers.action import start



async def main(): #всі компоненти для ініціалізації
    load_dotenv('.env')
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher(bot)

    start()



if __name__=="__main__":
    asyncio.run(main())