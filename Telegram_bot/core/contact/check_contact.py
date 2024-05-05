import sqlite3
from aiogram import types
from tp_project_vrm24_252.Telegram_bot.massage_config.messages import ContactMessage


async def add_contact_to_database(message, contact: types.Contact):
    is_ok = True
    try:
        connection = sqlite3.connect('contacts.db')
        cursor = connection.cursor()

        cursor.execute('''CREATE TABLE IF NOT EXISTS contacts
                              (user_id INTEGER PRIMARY KEY, phone_number TEXT)''')

        cursor.execute('''INSERT INTO contacts (user_id, phone_number)
                              VALUES (?, ?)''', (contact.user_id, contact.phone_number))

        connection.commit()
    except sqlite3.IntegrityError:
        await message.answer(f"Ой! я же тебя знаю, привет {message.from_user.first_name}!",
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
