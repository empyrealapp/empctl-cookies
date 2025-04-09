from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship

from emp_hooks.orm.base import DBModel

if TYPE_CHECKING:
    from .message import Message


class Chat(DBModel):
    __tablename__ = "chats"

    id: Mapped[int] = mapped_column(primary_key=True)
    type: Mapped[str] = mapped_column(nullable=False)

    messages: Mapped[list["Message"]] = relationship("Message", back_populates="chat")
