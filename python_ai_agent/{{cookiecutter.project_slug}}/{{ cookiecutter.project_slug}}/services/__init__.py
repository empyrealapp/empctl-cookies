from emp_hooks.orm import load_session

from ..models import Chat, Message, User
from .message import MessageService
from .user import UserService
from .chat import ChatService

session = load_session()

chat_service = ChatService(session, Chat)
message_service = MessageService(session, Message)
user_service = UserService(session, User)

__all__ = ["chat_service", "message_service", "user_service", "session"]
