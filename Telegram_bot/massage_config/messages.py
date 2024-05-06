class StartMessage:
    WELCOME_MESSAGE = (
        "<i>Мы ради видеть вас в чате!</i>"
    )
    INTRODUCTION_MESSAGE = (
        "Привет. Я - виртуальный помощник\n"
        "Могу рассказать про тариф и расходы, проверить баланс и также "
        "связать вас с нашими специалистами. Для этого предоставьте мне ваш номер в чат!"
    )


class SupportMessage:
    WELCOME_MESSAGE = (
        "Добрый день! Напишите ваш вопрос или описание проблемы одним сообщением."
    )
    NO_SUPPORT_REQUEST_MESSAGE = (
        "Вы не запросили поддержку. Воспользуйтесь командой /support."
    )
    SUPPORT_SUCCESS_MESSAGE = (
        "Ваш запрос отправлен администраторам. Ожидайте ответа."
    )


class ContactMessage:
    CONTACT_RECEIVED_MESSAGE = "Спасибо, ваш контакт получен!"
    PLEASE_SEND_CONTACT_MESSAGE = ("Пожалуйста, отправьте ваш контакт,"
                                   " чтобы мы могли связаться с вами.")


class InfoMessage:
    CONTACT_MISSING_MESSAGE = "Поделитесь вашим контактом с ботом"
    DATABASE_MISSING_MESSAGE = "Я о тебе ничего не знаю:("
    MESSAGE_USER_NOT_FOUND = "Вас нет в списке наших клиентов:( Пройдите регистрацию на сайте, пожалуйста."


class HelpMessage:
    HELP_TEXT = (
        "Список доступных команд:\n"
        "/start - Начать взаимодействие с ботом\n"
        "/help - Показать это сообщение со списком команд\n"
        "/info - Ваш профиль\n"
        "/support - отправить запрос в службу поддержки."
    )