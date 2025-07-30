from typing import List

from fastapi import APIRouter, Depends

from ...core.security import get_current_user
from ...models.user import UserIn, UserOut
from ...services.user_service import UserService, get_user_service

router = APIRouter()


@router.post("/", response_model=UserOut, status_code=201)
def create_user(user: UserIn, service: UserService = Depends(get_user_service), current_user: str = Depends(get_current_user)) -> UserOut:
    return service.create_user(user)


@router.get("/", response_model=List[UserOut])
def list_users(service: UserService = Depends(get_user_service), current_user: str = Depends(get_current_user)) -> List[UserOut]:
    return service.list_users()
