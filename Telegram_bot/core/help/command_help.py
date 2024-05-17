from aiogram.types import ReplyKeyboardRemove
from massage_config.messages import HelpMessage


async def get_help(message, state):
    await state.clear()
    await message.answer(HelpMessage.HELP_TEXT, reply_markup=ReplyKeyboardRemove())
