from aiogram import types


async def get_contact(message: types.Message):
    phone = message.contact.phone_number
    if message.contact.user_id == message.from_user.id:
        # TODO добавить его в БД и т.д. и т.п.
        await message.answer("Спасибо, ваш контакт получен!", reply_markup=None)
    else:
        await message.answer("Пожалуйста, отправьте ваш контакт, чтобы мы могли связаться с вами.")
