from abc import ABC, abstractmethod
from ..models.user import UserIn, UserOut
from typing import List


class UserRepository(ABC):
    @abstractmethod
    def create(self, user: UserIn) -> UserOut: ...

    @abstractmethod
    def list(self) -> List[UserOut]: ...
