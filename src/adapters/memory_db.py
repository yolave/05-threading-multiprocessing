from ..ports.db_port import UserRepository
from ..models.user import UserIn, UserOut


class MemoryUserRepository(UserRepository):
    def __init__(self):
        self.db: list[UserOut] = []
        self.counter = 1

    def create(self, user: UserIn) -> UserOut:
        user_out = UserOut(id=self.counter, **user.model_dump())
        self.db.append(user_out)
        self.counter += 1
        return user_out

    def list(self) -> list[UserOut]:
        return self.db