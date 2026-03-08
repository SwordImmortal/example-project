from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.sql import func

from app.core.database import Base


class NewsRecord(Base):
    """新闻记录模型"""

    __tablename__ = "news_records"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    content = Column(Text)
    source = Column(String(50))
    category = Column(String(50))
    url = Column(String(500))
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    def __repr__(self):
        return f"<NewsRecord(id={self.id}, title='{self.title}', source='{self.source}')>"
