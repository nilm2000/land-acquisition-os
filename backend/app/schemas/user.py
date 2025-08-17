from pydantic import BaseModel, EmailStr
from enum import Enum

class UserRole(str, Enum):
    admin = "admin"
    user = "user"

class UserBase(BaseModel):
    email: EmailStr
    full_name: str | None = None
    role: UserRole = UserRole.user

class UserCreate(UserBase):
    password: str

class UserRead(UserBase):
    id: int
    class Config:
        from_attributes = True

class LoginRequest(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
