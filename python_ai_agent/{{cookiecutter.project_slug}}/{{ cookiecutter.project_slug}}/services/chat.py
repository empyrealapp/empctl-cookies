from telegram import Message as TelegramMessage

from emp_hooks.orm import DBService

from {{ cookiecutter.project_slug }}.models import Chat


class ChatService(DBService[Chat]):
    def store_chat(self, message: TelegramMessage) -> Chat:
        return self.get_or_create(
            id=message.chat.id,
            type=message.chat.type,
        )
