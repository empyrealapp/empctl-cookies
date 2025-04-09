from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from emp_hooks.orm.base import DBModel

if TYPE_CHECKING:
    from .chat import Chat
    from .user import User


class Message(DBModel):
    __tablename__ = "messages"

    id: Mapped[int] = mapped_column(primary_key=True)
    chat_id: Mapped[int] = mapped_column(ForeignKey("chats.id"), nullable=False)
    message_id: Mapped[int] = mapped_column(nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    timestamp: Mapped[datetime] = mapped_column(nullable=False)
    text: Mapped[str] = mapped_column(nullable=False)

    chat: Mapped["Chat"] = relationship("Chat", back_populates="messages")
    user: Mapped["User"] = relationship("User", back_populates="messages")
