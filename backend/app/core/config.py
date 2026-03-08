from pydantic_settings import BaseSettings
from typing import Optional
import os


class Settings(BaseSettings):
    """应用配置"""

    # 应用信息
    APP_NAME: str = "Example Project API"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = True

    # 数据库配置
    DATABASE_URL: str = "postgresql+asyncpg://myuser:mypassword@localhost:5432/myapp"

    # Redis 配置
    REDIS_URL: str = "redis://localhost:6379/0"

    # 安全配置
    SECRET_KEY: str = "your-secret-key-change-in-production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7  # 7 天

    # CORS 配置
    BACKEND_CORS_ORIGINS: list = [
        "http://localhost:5173",
        "http://localhost:3000",
    ]

    # 外部 API 配置
    WEATHER_API_KEY: Optional[str] = None
    WEATHER_API_URL: str = "https://api.openweathermap.org/data/2.5/weather"

    # 分页配置
    DEFAULT_PAGE_SIZE: int = 20
    MAX_PAGE_SIZE: int = 100

    class Config:
        env_file = ".env"
        case_sensitive = True


# 全局配置实例
settings = Settings()
