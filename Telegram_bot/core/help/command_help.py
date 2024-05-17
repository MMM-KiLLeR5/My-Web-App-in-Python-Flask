from aiogram.types import ReplyKeyboardRemove
from tp_project_vrm24_252.Telegram_bot.massage_config.messages import HelpMessage


async def get_help(message, state):
    await state.clear()
    await message.answer(HelpMessage.HELP_TEXT, reply_markup=ReplyKeyboardRemove())
