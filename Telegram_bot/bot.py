from aiogram import Bot, Dispatcher
import asyncio
from aiogram.filters import Command
from core.contact.check_contact import get_contact
from core.help.command_help import get_help
from aiogram import F
from core.start.command_start import get_start
from core.support.command_support import send_support_request
from core.support.command_support import send_message_to_admins
from core.support.command_support import forward_admin_response_to_user
from core.info.command_info import get_user_info

TOKEN_API = "6749886611:AAFTQWO58ujk3z-wh-_hb4dl2DfO0GGmdbk"


async def start():
    bot = Bot(token=TOKEN_API)
    dp = Dispatcher()

    dp.message.register(get_start, Command(commands=['start']), F.chat.func(lambda chat: chat.id != -1002057587938))
    dp.message.register(get_help, Command(commands=['help']), F.chat.func(lambda chat: chat.id != -1002057587938))
    dp.message.register(get_user_info, Command(commands=['info']), F.chat.func(lambda chat: chat.id != -1002057587938))
    dp.message.register(get_contact, F.contact, F.chat.func(lambda chat: chat.id != -1002057587938))
    dp.message.register(send_support_request, Command(commands=['support']),
                        F.chat.func(lambda chat: chat.id != -1002057587938))
    dp.message.register(send_message_to_admins, F.chat.func(lambda chat: chat.id != -1002057587938))
    dp.message.register(forward_admin_response_to_user, F.chat.func(lambda chat: chat.id == -1002057587938))
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == '__main__':
    asyncio.run(start())

