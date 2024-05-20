from aiogram.fsm.state import StatesGroup, State
from aiogram import Bot, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.filters import Command
import os
from dotenv import load_dotenv
from massage_config.messages import SupportMessage

load_dotenv()

router = Router()


class SupportStates(StatesGroup):
    support_message = State()


@router.message(Command("support"))
async def send_support_request(message,  state: FSMContext):
    await state.set_state(state=SupportStates.support_message)
    await message.answer(SupportMessage.WELCOME_MESSAGE)


@router.message()
async def send_message_to_admins(message, bot: Bot, state: FSMContext):
    if await state.get_state() == SupportStates.support_message.state:
        await state.update_data(text_for_admin=message.text)
        admins_chat_id = int(os.getenv("ADMINS_CHAT_ID"))
        support_text = (
            f"Пользователь с ID {message.from_user.id} запрашивает поддержку:\n\n{message.text}"
        )
        await bot.send_message(admins_chat_id, support_text)
        await state.clear()
        await message.answer(SupportMessage.SUPPORT_SUCCESS_MESSAGE)
    else:
        await message.answer(SupportMessage.NO_SUPPORT_REQUEST_MESSAGE)


async def forward_admin_response_to_user(message: Message, bot: Bot):
    original_message_text = message.reply_to_message.text

    user_id_index = original_message_text.find("ID") + 3
    user_id = int(original_message_text[user_id_index:].split()[0])

    admin_response = message.text.strip()

    await bot.send_message(user_id, admin_response)

