from emp_hooks.orm import load_session

from ..models import Message, User
from .message import MessageService
from .user import UserService

session = load_session()

user_service = UserService(session, User)
message_service = MessageService(session, Message)

__all__ = ["user_service", "message_service"]
