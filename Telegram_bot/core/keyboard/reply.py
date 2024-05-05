from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, KeyboardButtonPollType

reply_keyboard = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text='Отправить контакт', request_contact=True)
    ]
], resize_keyboard=True, one_time_keyboard=True, input_field_placeholder='Отправь свой номер ↓', selective=True)