from aiogram.types import ReplyKeyboardRemove


async def get_help(message, state):
    await state.clear()
    help_text = (
        "Список доступных команд:\n"
        "/start - Начать взаимодействие с ботом\n"
        "/help - Показать это сообщение со списком команд\n"
        "/info - Ваш профиль\n"
        "/support - отправить запрос в службу поддержки."
    )

    await message.answer(help_text, reply_markup=ReplyKeyboardRemove())
