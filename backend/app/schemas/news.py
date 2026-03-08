from pydantic import BaseModel, HttpUrl
from typing import Optional
from datetime import datetime


class NewsBase(BaseModel):
    """新闻基础模型"""
    title: str
    content: Optional[str] = None
    source: Optional[str] = None
    category: Optional[str] = None
    url: Optional[HttpUrl] = None


class NewsCreate(NewsBase):
    """新闻创建模型"""
    pass


class News(NewsBase):
    """新闻响应模型"""
    id: int
    created_at: datetime

    class Config:
        from_attributes = True


class NewsList(BaseModel):
    """新闻列表响应包装"""
    code: int = 0
    message: str = "success"
    data: list[News]
