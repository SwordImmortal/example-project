from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import Optional, List
import random

from app.core.database import get_db
from app.models.news import NewsRecord
from app.schemas.news import (
    NewsCreate,
    NewsList,
    News as NewsSchema
)

router = APIRouter(prefix="/api/v1/news", tags=["新闻"])


def generate_mock_news(count: int = 10) -> List[dict]:
    """生成模拟新闻数据（实际项目中应调用新闻 API 或爬虫）"""
    categories = ["科技", "AI", "编程", "生活", "健康"]
    sources = ["Hacker News", "GitHub Trending", "36氪", "腾讯科技", "新浪科技"]
    titles = [
        "AI 技术突破：新模型性能提升 50%",
        "Claude 4 发布，能力全面超越 GPT-4",
        "Python 4.0 计划公布，性能提升显著",
        "Web 开发新趋势：Vue 4 带来革命性变化",
        "FastAPI 1.0 发布，成为 Python Web 首选",
        "Docker 和 Kubernetes 最佳实践指南",
        "机器学习入门：从零开始掌握核心概念",
        "TypeScript 5.4 新特性详解",
        "前端性能优化：让你的网站快 10 倍",
        "数据库设计：PostgreSQL vs MySQL 对比",
    ]

    news_list = []
    for _ in range(count):
        news_list.append({
            "title": random.choice(titles),
            "content": "这是一篇关于科技新闻的详细内容...",
            "source": random.choice(sources),
            "category": random.choice(categories),
            "url": f"https://example.com/news/{random.randint(1000, 9999)}"
        })

    return news_list


@router.get("/", response_model=NewsList)
async def get_news(
    category: Optional[str] = Query(None, description="新闻分类"),
    source: Optional[str] = Query(None, description="新闻来源"),
    limit: Optional[int] = Query(10, ge=1, le=50, description="返回数量"),
    db: AsyncSession = Depends(get_db)
):
    """获取新闻列表"""
    # 构建查询
    query = select(NewsRecord)

    if category:
        query = query.where(NewsRecord.category == category)
    if source:
        query = query.where(NewsRecord.source == source)

    query = query.order_by(NewsRecord.created_at.desc()).limit(limit)

    # 执行查询
    result = await db.execute(query)
    news_records = result.scalars().all()

    # 如果数据库中没有记录，生成模拟数据
    if not news_records:
        mock_news = generate_mock_news(limit)
        for news_data in mock_news:
            db_news = NewsRecord(**news_data)
            db.add(db_news)

        await db.commit()

        # 重新查询
        result = await db.execute(query)
        news_records = result.scalars().all()

    return NewsList(code=0, message="success", data=news_records)


@router.get("/{news_id}", response_model=dict)
async def get_news_detail(
    news_id: int,
    db: AsyncSession = Depends(get_db)
):
    """获取新闻详情"""
    result = await db.execute(
        select(NewsRecord).where(NewsRecord.id == news_id)
    )
    news = result.scalar_one_or_none()

    if not news:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"新闻 ID {news_id} 不存在"
        )

    return {
        "code": 0,
        "message": "success",
        "data": news
    }


@router.post("/scrape", response_model=dict)
async def scrape_news(
    category: Optional[str] = Query("科技", description="抓取的分类"),
    db: AsyncSession = Depends(get_db)
):
    """抓取新闻（模拟接口）"""
    # 生成模拟新闻数据
    mock_news = generate_mock_news(5)

    # 保存到数据库
    created_count = 0
    for news_data in mock_news:
        news_data["category"] = category
        db_news = NewsRecord(**news_data)
        db.add(db_news)
        created_count += 1

    await db.commit()

    return {
        "code": 0,
        "message": f"成功抓取 {created_count} 条新闻",
        "data": {
            "created_count": created_count,
            "category": category
        }
    }
