import sqlite3
from aiogram import types
from massage_config.messages import ContactMessage


async def add_contact_to_database(message, contact: types.Contact):
    is_ok = True
    try:
        connection = sqlite3.connect('contacts.db')
        cursor = connection.cursor()

        cursor.execute(ContactMessage.CREATE_TABLE_QUERY)

        cursor.execute(ContactMessage.INSERT_CONTACT_QUERY, (contact.user_id, contact.phone_number))

        connection.commit()
    except sqlite3.IntegrityError:
        await message.answer(f"{ContactMessage.GREETING_MESSAGE} {message.from_user.first_name}!",
                             reply_markup=types.ReplyKeyboardRemove())
        is_ok = False
    finally:
        connection.close()
    return is_ok


async def get_contact(message: types.Message, bot):
    contact = message.contact

    if contact.user_id == message.from_user.id:
        is_ok = await add_contact_to_database(message, contact)
        if is_ok:
            await message.answer(ContactMessage.CONTACT_RECEIVED_MESSAGE,
                                 reply_markup=types.ReplyKeyboardRemove())
    else:
        await message.answer(ContactMessage.PLEASE_SEND_CONTACT_MESSAGE)
