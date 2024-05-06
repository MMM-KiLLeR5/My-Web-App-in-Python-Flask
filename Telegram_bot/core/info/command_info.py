import sqlite3
import aiohttp
import os
from dotenv import load_dotenv
from tp_project_vrm24_252.Telegram_bot.massage_config.messages import InfoMessage

load_dotenv()


async def fetch_user_info(phone_number):
    url = f'{os.getenv("URL_USERS_PHONE_NUMBER")}{phone_number}'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 406:
                return False
            else:
                return await response.json()


async def get_user_info(message, state):
    await state.clear()
    try:
        connection = sqlite3.connect('contacts.db')
        cursor = connection.cursor()

        cursor.execute('''SELECT phone_number FROM contacts WHERE user_id = ?''', (message.from_user.id,))
        result = cursor.fetchone()

        if result:
            phone_number = result[0]
            user_info = await fetch_user_info(phone_number)
            if not user_info:
                await message.answer(InfoMessage.MESSAGE_USER_NOT_FOUND)
            else:
                response_text = f"Номер телефона: {phone_number}\n" \
                                f"Баланс: {user_info['balance']}руб.\n" \
                                f"Цена за 1 Гб: {user_info['cost_one_gb']}\n" \
                                f"Цена за 1 минуту: {user_info['cost_one_minute']}\n" \
                                f"Гб: {user_info['gb']}\n" \
                                f"Минуты: {user_info['minute']}\n" \
                                f"Цена: {user_info['price']}руб.\n" \
                                f"Гб пользователя: {user_info['user_gbs']}\n" \
                                f"Минуты пользователя: {user_info['user_minutes']}"
                await message.answer(response_text)
        else:
            await message.answer(InfoMessage.CONTACT_MISSING_MESSAGE)
    except sqlite3.OperationalError:
        await message.answer(InfoMessage.DATABASE_MISSING_MESSAGE)
    finally:
        connection.close()
