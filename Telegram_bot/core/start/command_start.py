import asyncio
from ..keyboard.reply import reply_keyboard
from ..utils.commands import set_commands
from tp_project_vrm24_252.Telegram_bot.massage_config.messages import StartMessage


async def get_start(message, bot, state):
    await state.clear()
    await set_commands(bot)
    await message.answer(StartMessage.WELCOME_MESSAGE, parse_mode='HTML')
    await asyncio.sleep(0.7)
    await message.answer(StartMessage.INTRODUCTION_MESSAGE, reply_markup=reply_keyboard)