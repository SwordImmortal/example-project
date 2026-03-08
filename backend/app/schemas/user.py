from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime


class UserBase(BaseModel):
    """用户基础模型"""
    username: str
    email: EmailStr


class UserCreate(UserBase):
    """用户创建模型"""
    password: str


class UserUpdate(BaseModel):
    """用户更新模型"""
    email: Optional[EmailStr] = None
    password: Optional[str] = None


class UserLogin(BaseModel):
    """用户登录模型"""
    username: str
    password: str


class User(UserBase):
    """用户响应模型"""
    id: int
    is_active: bool
    is_superuser: bool
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True


class UserResponse(BaseModel):
    """用户响应包装"""
    code: int = 0
    message: str = "success"
    data: User


class Token(BaseModel):
    """令牌模型"""
    access_token: str
    token_type: str = "bearer"


class TokenResponse(BaseModel):
    """令牌响应包装"""
    code: int = 0
    message: str = "success"
    data: Token
