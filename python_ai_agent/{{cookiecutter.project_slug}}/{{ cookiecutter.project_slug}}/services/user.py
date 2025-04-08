from emp_hooks.orm import DBService

from ..models import User


class UserService(DBService[User]):
    pass
