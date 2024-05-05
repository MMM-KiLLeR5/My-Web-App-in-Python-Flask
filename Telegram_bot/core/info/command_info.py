import sqlite3


async def get_user_info(message, state):
    await state.clear()
    try:
        connection = sqlite3.connect('contacts.db')
        cursor = connection.cursor()

        cursor.execute('''SELECT phone_number FROM contacts WHERE user_id = ?''', (message.from_user.id,))
        result = cursor.fetchone()

        if result:
            phone_number = result[0]
            await message.answer(phone_number)
        else:
            await message.answer("Поделитесь вашим контактом с ботом")
    except sqlite3.OperationalError:
        await message.answer("Я о тебе ничего не знаю:(")
    finally:
        connection.close()
