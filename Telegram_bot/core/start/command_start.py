import asyncio

from ..keyboard.reply import reply_keyboard
from ..utils.commands import set_commands


async def get_start(message, bot):
    await set_commands(bot)
    await message.answer(f'<i>Мы ради видеть вас в чате!</i>', parse_mode='HTML')
    await asyncio.sleep(0.7)
    await message.answer(
        f'Привет. Я - виртуальный помощник\n'
        f'Могу рассказать про тариф и расходы, проверить баланс и также'
        f' связать вас с нашими специалистами. Для этого предоставьте мне ваш номер в чат!',
        reply_markup=reply_keyboard
    )