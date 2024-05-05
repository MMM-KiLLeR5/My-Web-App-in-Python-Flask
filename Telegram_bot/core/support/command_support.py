from aiogram.fsm.state import StatesGroup, State
from aiogram import Bot, types, Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.filters import Command
from aiogram import Dispatcher

router = Router()


class SupportStates(StatesGroup):
    support_message = State()


@router.message(Command("support"))
async def send_support_request(message, bot: Bot, state: FSMContext):
    await state.set_state(state=SupportStates.support_message)
    await message.answer("Добрый день! Напишите ваш вопрос или описание проблемы одним сообщением.")


@router.message()
async def send_message_to_admins(message, bot, state: FSMContext):
    if await state.get_state() == SupportStates.support_message.state:
        await state.update_data(text_for_admin=message.text)
        admins_chat_id = -1002057587938
        support_text = f"Пользователь с ID {message.from_user.id} запрашивает поддержку:\n\n{message.text}"
        await bot.send_message(admins_chat_id, support_text)
        await state.clear()
        await message.answer("Ваш запрос отправлен администраторам. Ожидайте ответа.")
    else:
        await message.answer("Вы не запросили поддержку. Воспользуйтесь командой /support.")


async def forward_admin_response_to_user(message: Message, bot: Bot, state: FSMContext):
    original_message_text = message.reply_to_message.text

    user_id_index = original_message_text.find("ID") + 3
    user_id = int(original_message_text[user_id_index:].split()[0])

    admin_response = message.text.strip()

    await bot.send_message(user_id, admin_response)

