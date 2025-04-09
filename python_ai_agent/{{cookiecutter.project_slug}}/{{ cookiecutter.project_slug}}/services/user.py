from telegram import User as TelegramUser

from emp_hooks.orm import DBService
from emp_hooks.handlers.telegram import ContextTypes

from {{ cookiecutter.project_slug }}.models import User


class UserService(DBService[User]):
    def load_bot(self, context: ContextTypes.DEFAULT_TYPE) -> User:
        return self.get_or_create(
            id=context.bot.id,
            username=context.bot.username,
            first_name=context.bot.first_name,
            last_name=context.bot.last_name,
        )

    def store_user(self, user: TelegramUser):
        return self.get_or_create(
            id=user.id,
            username=user.username,
            first_name=user.first_name,
            last_name=user.last_name,
        )
