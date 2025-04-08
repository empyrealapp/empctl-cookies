from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship

from emp_hooks.orm.base import DBModel

if TYPE_CHECKING:
    from .message import Message


class User(DBModel):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(nullable=True)

    messages: Mapped[list["Message"]] = relationship("Message", back_populates="user")
