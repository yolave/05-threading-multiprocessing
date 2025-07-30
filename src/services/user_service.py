from ..models.user import UserIn, UserOut
from ..ports.db_port import UserRepository
from ..adapters.memory_db import MemoryUserRepository
from typing import List


class UserService:
    def __init__(self, repo: UserRepository):
        self.repo = repo

    def create_user(self, user: UserIn) -> UserOut:
        return self.repo.create(user)

    def list_users(self) -> List[UserOut]:
        return self.repo.list()


user_service = UserService(MemoryUserRepository())


def get_user_service() -> UserService:
    return user_service
