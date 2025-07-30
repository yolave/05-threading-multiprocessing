from pydantic import BaseModel, EmailStr


class UserIn(BaseModel):
    name: str
    email: EmailStr


class UserOut(UserIn):
    id: int
