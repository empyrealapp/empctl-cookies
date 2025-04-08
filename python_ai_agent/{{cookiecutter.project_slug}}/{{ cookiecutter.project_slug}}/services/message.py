from datetime import datetime, timezone

from sqlalchemy import select

from emp_hooks.orm import DBService

from {{ cookiecutter.project_slug }}.models import Message


class MessageService(DBService[Message]):
    def get_latest_message(
        self, user_id: list[int] | int, limit: int = 10,
    ) -> list[Message]:
        if isinstance(user_id, int):
            user_id = [user_id]
        stmt = select(Message).where(Message.user_id.in_(user_id))
        stmt = stmt.order_by(Message.timestamp.desc()).limit(limit)
        # reverse the list to get the earliest messages first
        return list(self.session.scalars(stmt))[::-1]
    
    def add_message(self, content: str, user_id: int):
        now = datetime.now(timezone.utc)
        message = Message(content=content, user_id=user_id, timestamp=now)
        self.session.add(message)
        self.session.commit()
        return message
