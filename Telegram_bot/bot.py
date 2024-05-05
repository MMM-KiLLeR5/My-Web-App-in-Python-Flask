from aiogram import Bot, Dispatcher
import asyncio
from aiogram.filters import Command
from core.contact.check_contact import get_contact
from core.help.command_help import get_help
from aiogram import F
from core.start.command_start import get_start

TOKEN_API = "6749886611:AAFTQWO58ujk3z-wh-_hb4dl2DfO0GGmdbk"


async def start():
    bot = Bot(token=TOKEN_API)
    dp = Dispatcher()

    dp.message.register(get_start, Command(commands=['start']))
    dp.message.register(get_help, Command(commands=['help']))
    dp.message.register(get_contact, F.contact)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == '__main__':
    asyncio.run(start())

