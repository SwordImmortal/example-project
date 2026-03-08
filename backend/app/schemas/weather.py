from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class WeatherBase(BaseModel):
    """天气基础模型"""
    city: str
    temperature: int = Field(..., description="温度（摄氏度）")
    humidity: int = Field(..., ge=0, le=100, description="湿度（百分比）")
    description: str


class WeatherCreate(WeatherBase):
    """天气创建模型"""
    pass


class Weather(WeatherBase):
    """天气响应模型"""
    id: int
    created_at: datetime

    class Config:
        from_attributes = True


class WeatherResponse(BaseModel):
    """天气响应包装"""
    code: int = 0
    message: str = "success"
    data: Weather


class WeatherHistory(BaseModel):
    """天气历史模型"""
    city: str
    avg_temperature: Optional[float] = None
    records: list[Weather]


class WeatherHistoryResponse(BaseModel):
    """天气历史响应包装"""
    code: int = 0
    message: str = "success"
    data: WeatherHistory
