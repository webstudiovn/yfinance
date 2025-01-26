import asyncio, logging
from aiogram import Bot, Dispatcher
from core.settings import dbconfigs
from headlers import commands
from utils.commands import set_commands

bot = Bot(token=dbconfigs.token_telegram_bot)

dp = Dispatcher()

async def main():
    await set_commands(bot)
    dp.include_router(commands.router)
    await dp.start_polling(bot)


logging.basicConfig(level=logging.INFO)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот вышел из чата!")