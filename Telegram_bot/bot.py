from aiogram import Bot, Dispatcher
import asyncio
from aiogram.filters import Command
from aiogram import F
import os
from dotenv import load_dotenv

from core.contact.check_contact import get_contact
from core.help.command_help import get_help
from core.start.command_start import get_start
from core.support.command_support import (
    send_support_request,
    send_message_to_admins,
    forward_admin_response_to_user
)
from core.info.command_info import get_user_info

load_dotenv()

TOKEN_API = os.getenv("TOKEN_API")


async def start():
    bot = Bot(token=TOKEN_API)
    dp = Dispatcher()

    admin_chat_id = int(os.getenv("ADMINS_CHAT_ID"))

    dp.message.register(get_start, Command(commands=['start']),
                        F.chat.func(lambda chat: chat.id != admin_chat_id))
    dp.message.register(get_help, Command(commands=['help']),
                        F.chat.func(lambda chat: chat.id != admin_chat_id))
    dp.message.register(get_user_info, Command(commands=['info']),
                        F.chat.func(lambda chat: chat.id != admin_chat_id))
    dp.message.register(get_contact, F.contact,
                        F.chat.func(lambda chat: chat.id != admin_chat_id))
    dp.message.register(send_support_request, Command(commands=['support']),
                        F.chat.func(lambda chat: chat.id != admin_chat_id))
    dp.message.register(send_message_to_admins,
                        F.chat.func(lambda chat: chat.id != admin_chat_id))
    dp.message.register(forward_admin_response_to_user,
                        F.chat.func(lambda chat: chat.id == admin_chat_id))
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == '__main__':
    asyncio.run(start())
