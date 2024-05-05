from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_commands(bot: Bot):
    commands = [
        BotCommand(
            command='start',
            description='Перезапустить'
        ),
        BotCommand(
            command='help',
            description='Помощь'
        ),
        BotCommand(
            command='info',
            description='Мой профиль'
        ),
        BotCommand(
            command='support',
            description='Поддержка'
        )
    ]

    await bot.set_my_commands(commands, BotCommandScopeDefault())
