from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault

async def set_commands(bot: Bot):
    commands = [
        BotCommand(
            command="start", 
            description="Запустить бота"
        ),
        BotCommand(
            command="ticker",
            description="Получить акцию"
        ),
        BotCommand(
            command="editgoogle",
            description="Редактирование таблицы"
        ),
        BotCommand(
            command="mytickers",
            description="Мои акции"
        )
    ]

    await bot.set_my_commands(commands, BotCommandScopeDefault())