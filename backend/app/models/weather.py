from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func

from app.core.database import Base


class WeatherRecord(Base):
    """天气记录模型"""

    __tablename__ = "weather_records"

    id = Column(Integer, primary_key=True, index=True)
    city = Column(String(50), index=True, nullable=False)
    temperature = Column(Integer, nullable=False)
    humidity = Column(Integer, nullable=False)
    description = Column(String(100), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    def __repr__(self):
        return f"<WeatherRecord(id={self.id}, city='{self.city}', temp={self.temperature}°C)>"
