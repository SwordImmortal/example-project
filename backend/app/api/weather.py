from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func
from sqlalchemy.orm import selectinload
from typing import Optional
from datetime import datetime, timedelta
import random

from app.core.database import get_db
from app.models.weather import WeatherRecord
from app.schemas.weather import (
    WeatherCreate,
    WeatherResponse,
    WeatherHistory,
    WeatherHistoryResponse
)
from app.api.users import get_current_user
from app.models.user import User

router = APIRouter(prefix="/api/v1/weather", tags=["天气"])


def generate_mock_weather(city: str) -> dict:
    """生成模拟天气数据（实际项目中应调用天气 API）"""
    return {
        "city": city,
        "temperature": random.randint(15, 35),
        "humidity": random.randint(30, 80),
        "description": random.choice([
            "晴", "多云", "阴", "小雨", "中雨", "大雨", "雷阵雨"
        ])
    }


@router.get("/{city}", response_model=WeatherResponse)
async def get_weather(
    city: str,
    db: AsyncSession = Depends(get_db)
):
    """获取指定城市的当前天气"""
    # 模拟天气 API 调用
    weather_data = generate_mock_weather(city)

    # 保存到数据库
    db_weather = WeatherRecord(**weather_data)
    db.add(db_weather)
    await db.commit()
    await db.refresh(db_weather)

    return WeatherResponse(code=0, message="success", data=db_weather)


@router.get("/history/{city}", response_model=WeatherHistoryResponse)
async def get_weather_history(
    city: str,
    days: Optional[int] = Query(7, ge=1, le=30, description="查询天数"),
    db: AsyncSession = Depends(get_db)
):
    """获取指定城市的历史天气"""
    # 计算时间范围
    end_date = datetime.utcnow()
    start_date = end_date - timedelta(days=days)

    # 查询历史记录
    result = await db.execute(
        select(WeatherRecord)
        .where(
            WeatherRecord.city == city,
            WeatherRecord.created_at >= start_date
        )
        .order_by(WeatherRecord.created_at.desc())
    )
    records = result.scalars().all()

    if not records:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"未找到城市 '{city}' 的天气记录"
        )

    # 计算平均温度
    avg_temp = sum(r.temperature for r in records) / len(records)

    return WeatherHistoryResponse(
        code=0,
        message="success",
        data=WeatherHistory(
            city=city,
            avg_temperature=round(avg_temp, 1),
            records=records
        )
    )


@router.post("/subscribe", response_model=dict)
async def subscribe_weather(
    city: str = Query(..., description="城市名称"),
    current_user: Annotated[User, Depends(get_current_user)] = None
):
    """订阅城市天气（示例接口）"""
    # 实际项目中，这里应该将订阅关系保存到数据库
    return {
        "code": 0,
        "message": f"成功订阅城市 '{city}' 的天气",
        "data": {
            "city": city,
            "user_id": current_user.id if current_user else None
        }
    }
