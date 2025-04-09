from emp_hooks.orm import DBService
from sqlalchemy import select
from telegram import Message as TelegramMessage

from {{ cookiecutter.project_slug }}.models import Chat, Message, User


class MessageService(DBService[Message]):
    def get_latest_message(
        self, chat_id: int, user_id: int | None = None, limit: int = 10
    ) -> list[Message]:
        stmt = select(Message).where(Message.chat_id == chat_id)
        if user_id:
            stmt = stmt.where(Message.user_id == user_id)

        stmt = stmt.order_by(Message.timestamp.desc()).limit(limit)
        return list(self.session.scalars(stmt))[::-1]

    def add_message(
        self,
        chat: Chat,
        user: User,
        message: TelegramMessage,
    ):
        return self.get_or_create(
            chat_id=chat.id,
            message_id=message.message_id,
            text=message.text,
            user_id=user.id,
            timestamp=message.date,
        )
