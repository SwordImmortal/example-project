# 示例项目技术说明文档

> 本文档详细说明整个项目的技术架构，帮助你理解现代化 Web 应用的完整技术栈。

---

## 📖 目录

1. [项目概述](#1-项目概述)
2. [技术选型](#2-技术选型)
3. [架构设计](#3-架构设计)
4. [前后端通信](#4-前后端通信)
5. [数据库设计](#5-数据库设计)
6. [安全机制](#6-安全机制)
7. [部署方案](#7-部署方案)
8. [开发工作流](#8-开发工作流)
9. [常见问题](#9-常见问题)

---

## 1. 项目概述

### 1.1 项目目标

这是一个**完整的现代化 Web 应用示例**，展示了：

- ✅ 前后端分离架构
- ✅ RESTful API 设计
- ✅ 用户认证系统（JWT）
- ✅ 数据持久化（PostgreSQL）
- ✅ 缓存机制（Redis）
- ✅ 响应式前端界面

### 1.2 核心功能

| 功能模块 | 描述 |
|----------|------|
| **用户管理** | 注册、登录、个人信息管理 |
| **天气查询** | 实时天气、历史天气、订阅通知 |
| **新闻推送** | 新闻列表、分类筛选、定时抓取 |

---

## 2. 技术选型

### 2.1 为什么选择这些技术？

```
┌─────────────────────────────────────────────────────────┐
│                    技术选型原则                           │
│  1. 成熟稳定（有大量生产案例）                            │
│  2. 社区活跃（遇到问题能快速解决）                        │
│  3. 中文文档友好（国内开发者友好）                        │
│  4. Claude 支持好（AI 辅助编程效率高）                    │
└─────────────────────────────────────────────────────────┘
```

### 2.2 前端技术栈

| 技术 | 选择理由 | 国内成熟度 |
|------|----------|------------|
| **Vue 3** | 学习曲线平缓、中文文档完善、生态成熟 | ⭐⭐⭐⭐⭐ |
| **TypeScript** | 类型安全、减少运行时错误 | ⭐⭐⭐⭐ |
| **Vite** | 开发体验极佳、热更新快 | ⭐⭐⭐⭐⭐ |
| **Ant Design Vue** | 企业级 UI 组件、设计规范 | ⭐⭐⭐⭐⭐ |

### 2.3 后端技术栈

| 技术 | 选择理由 | 国内成熟度 |
|------|----------|------------|
| **FastAPI** | 高性能、异步原生、自动生成文档 | ⭐⭐⭐⭐⭐ |
| **SQLAlchemy** | Python 最成熟的 ORM | ⭐⭐⭐⭐⭐ |
| **PostgreSQL** | 功能强大的关系型数据库 | ⭐⭐⭐⭐⭐ |
| **Redis** | 高性能缓存/消息队列 | ⭐⭐⭐⭐⭐ |

---

## 3. 架构设计

### 3.1 整体架构图

```
┌─────────────────────────────────────────────────────────────┐
│                        客户端层                               │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐   │
│  │   浏览器      │  │   移动端      │  │   小程序      │   │
│  └──────────────┘  └──────────────┘  └──────────────┘   │
└───────────────────────┬─────────────────────────────────────┘
                        │ HTTP/JSON
                        ▼
┌─────────────────────────────────────────────────────────────┐
│                        API 网关层                            │
│  ┌──────────────────────────────────────────────────────┐ │
│  │              Nginx / Kong (可选)                     │ │
│  │              负载均衡、限流、SSL                       │ │
│  └──────────────────────────────────────────────────────┘ │
└───────────────────────┬─────────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────────┐
│                        应用层                               │
│  ┌──────────────────────────────────────────────────────┐ │
│  │                    FastAPI                           │ │
│  │  ┌──────────┐  ┌──────────┐  ┌──────────┐         │ │
│  │  │ 用户路由  │  │ 天气路由  │  │ 新闻路由  │         │ │
│  │  └──────────┘  └──────────┘  └──────────┘         │ │
│  │  ┌──────────────────────────────────────────────┐  │ │
│  │  │         业务逻辑层（Services）                │  │ │
│  │  └──────────────────────────────────────────────┘  │ │
│  │  ┌──────────────────────────────────────────────┐  │ │
│  │  │         数据访问层（CRUD）                    │  │ │
│  │  └──────────────────────────────────────────────┘  │ │
│  └──────────────────────────────────────────────────────┘ │
└───────────────────────┬─────────────────────────────────────┘
                        │
        ┌───────────────┼───────────────┐
        ▼               ▼               ▼
┌──────────────┐  ┌──────────┐  ┌──────────────┐
│ PostgreSQL   │  │  Redis   │  │  外部 API    │
│  (主数据库)   │  │  (缓存)   │  │ (天气/新闻)  │
└──────────────┘  └──────────┘  └──────────────┘
```

### 3.2 前端架构

```
D:\coding\example-project\frontend\
├── src/
│   ├── api/           # API 调用层
│   ├── components/    # 可复用组件
│   ├── views/         # 页面组件
│   ├── stores/        # 状态管理（Pinia）
│   ├── router/        # 路由配置
│   └── main.ts        # 应用入口
├── public/            # 静态资源
└── package.json       # 依赖配置
```

**核心概念：**

| 概念 | 说明 | 示例 |
|------|------|------|
| **组件** | 可复用的 UI 片段 | `<WeatherCard />` |
| **路由** | 页面导航映射 | `/weather` → `Weather.vue` |
| **状态管理** | 全局数据共享 | 用户登录状态 |
| **API 调用** | 与后端交互 | `axios.get('/api/v1/weather')` |

### 3.3 后端架构

```
D:\coding\example-project\backend\
├── app/
│   ├── api/           # API 路由层（定义接口）
│   ├── core/          # 核心配置（数据库、安全）
│   ├── models/        # 数据库模型（表结构）
│   ├── schemas/       # Pydantic 模型（数据验证）
│   ├── services/      # 业务逻辑层
│   └── utils/         # 工具函数
├── tests/             # 测试文件
├── main.py            # 应用入口
└── requirements.txt   # 依赖配置
```

**核心概念：**

| 概念 | 说明 | 示例 |
|------|------|------|
| **路由** | API 端点定义 | `@router.get("/weather/{city}")` |
| **模型** | 数据库表映射 | `class WeatherRecord(Base)` |
| **Schema** | 请求/响应验证 | `class WeatherCreate(BaseModel)` |
| **依赖注入** | 自动注入参数 | `db: AsyncSession = Depends(get_db)` |

---

## 4. 前后端通信

### 4.1 通信流程

```
前端                              后端
  │                                  │
  │  1. 用户点击"查询天气"             │
  ├─────────────────────────────────>│
  │  GET /api/v1/weather/shanghai   │
  │                                  │
  │  2. 返回 JSON 数据                │
  │<─────────────────────────────────┤
  │  {"code": 0, "data": {...}}     │
  │                                  │
  │  3. 渲染页面                      │
  │  ──────────────────────────────> │
  │                                  │
```

### 4.2 请求格式

```json
// 请求
GET /api/v1/weather/shanghai

// 响应
{
  "code": 0,
  "message": "success",
  "data": {
    "id": 1,
    "city": "上海",
    "temperature": 25,
    "humidity": 60,
    "description": "晴",
    "created_at": "2026-03-08T10:00:00"
  }
}
```

### 4.3 CORS 配置

```python
# backend/main.py
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # 前端地址
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

---

## 5. 数据库设计

### 5.1 数据库表结构

#### 用户表 (users)

| 字段 | 类型 | 说明 | 示例 |
|------|------|------|------|
| id | INTEGER | 主键 | 1 |
| username | VARCHAR(50) | 用户名（唯一） | "zhangsan" |
| email | VARCHAR(100) | 邮箱（唯一） | "zhangsan@example.com" |
| hashed_password | VARCHAR(255) | 加密密码 | "$2b$12$..." |
| is_active | BOOLEAN | 是否激活 | true |
| is_superuser | BOOLEAN | 是否管理员 | false |
| created_at | TIMESTAMP | 创建时间 | "2026-03-08 10:00:00" |
| updated_at | TIMESTAMP | 更新时间 | "2026-03-08 11:00:00" |

#### 天气表 (weather_records)

| 字段 | 类型 | 说明 | 示例 |
|------|------|------|------|
| id | INTEGER | 主键 | 1 |
| city | VARCHAR(50) | 城市 | "上海" |
| temperature | INTEGER | 温度（℃） | 25 |
| humidity | INTEGER | 湿度（%） | 60 |
| description | VARCHAR(100) | 天气描述 | "晴" |
| created_at | TIMESTAMP | 记录时间 | "2026-03-08 10:00:00" |

#### 新闻表 (news_records)

| 字段 | 类型 | 说明 | 示例 |
|------|------|------|------|
| id | INTEGER | 主键 | 1 |
| title | VARCHAR(255) | 标题 | "AI 技术突破" |
| content | TEXT | 内容 | "详细内容..." |
| source | VARCHAR(50) | 来源 | "36氪" |
| category | VARCHAR(50) | 分类 | "科技" |
| url | VARCHAR(500) | 链接 | "https://..." |
| created_at | TIMESTAMP | 创建时间 | "2026-03-08 10:00:00" |

### 5.2 数据库关系

```
┌──────────┐
│  users   │
└──────────┘
            │ (用户可以订阅天气/新闻)
            ▼
     ┌──────┴──────┐
     │             │
┌──────────┐  ┌──────────┐
│ weather  │  │  news    │
└──────────┘  └──────────┘
```

### 5.3 数据库操作

```python
# 创建用户
user = User(username="zhangsan", email="zhangsan@example.com", ...)
db.add(user)
await db.commit()

# 查询用户
result = await db.execute(select(User).where(User.username == "zhangsan"))
user = result.scalar_one_or_none()

# 更新用户
user.email = "new@example.com"
await db.commit()

# 删除用户
await db.delete(user)
await db.commit()
```

---

## 6. 安全机制

### 6.1 用户认证流程

```
用户                              服务器
  │                                  │
  │  1. 输入用户名/密码               │
  ├─────────────────────────────────>│
  │  POST /api/v1/users/login        │
  │                                  │
  │  2. 验证密码                      │
  │                                  │
  │  3. 生成 JWT Token                │
  │<─────────────────────────────────┤
  │  {"access_token": "eyJ...", ...} │
  │                                  │
  │  4. 保存 Token 到 localStorage    │
  │  ──────────────────────────────> │
  │                                  │
  │  5. 后续请求带上 Token            │
  ├─────────────────────────────────>│
  │  Authorization: Bearer eyJ...    │
  │                                  │
```

### 6.2 密码加密

```python
# 加密密码
hashed_password = get_password_hash("mypassword")
# 输出: $2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewY5GyWQ9qOyDk6

# 验证密码
is_valid = verify_password("mypassword", hashed_password)
# 输出: True
```

### 6.3 JWT Token

```python
# 生成 Token
token = create_access_token(data={"sub": "zhangsan"})

# 解码 Token
payload = decode_access_token(token)
# 输出: {"sub": "zhangsan", "exp": 1234567890}
```

---

## 7. 部署方案

### 7.1 开发环境

```bash
# 1. 启动数据库
docker-compose up -d postgres redis

# 2. 启动后端
cd backend
pip install -r requirements.txt
python main.py

# 3. 启动前端
cd frontend
npm install
npm run dev
```

### 7.2 生产环境

#### 方案 A：云服务商托管

| 服务 | 推荐平台 | 费用 |
|------|----------|------|
| 前端 | Vercel / Netlify | 免费或少量费用 |
| 后端 | Railway / Render | 按量付费 |
| 数据库 | Supabase / 阿里云 RDS | 按规格付费 |

#### 方案 B：自建服务器

```bash
# 服务器配置
- CPU: 2 核
- 内存: 4GB
- 硬盘: 40GB SSD
- 系统: Ubuntu 22.04

# 部署步骤
1. 安装 Docker
2. 拉取项目代码
3. 配置环境变量
4. 运行 docker-compose up -d
5. 配置 Nginx 反向代理
6. 配置 SSL 证书
```

### 7.3 Docker 部署

```yaml
# docker-compose.yml
services:
  postgres:
    image: postgres:16-alpine
    environment:
      POSTGRES_USER: myuser
      POSTGRES_PASSWORD: mypassword
      POSTGRES_DB: myapp
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data

  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"
    volumes:
      - redis_data:/data

  backend:
    build: ./backend
    ports:
      - "8000:8000"
    environment:
      DATABASE_URL: postgresql+asyncpg://myuser:mypassword@postgres:5432/myapp
      REDIS_URL: redis://redis:6379/0
    depends_on:
      - postgres
      - redis

  frontend:
    build: ./frontend
    ports:
      - "5173:80"
    depends_on:
      - backend
```

---

## 8. 开发工作流

### 8.1 本地开发流程

```bash
# 1. 拉取最新代码
git pull origin main

# 2. 安装依赖
cd backend && pip install -r requirements.txt
cd ../frontend && npm install

# 3. 启动服务
docker-compose up -d  # 数据库
python main.py        # 后端（终端1）
npm run dev          # 前端（终端2）

# 4. 开发功能
# ... 编写代码 ...

# 5. 运行测试
pytest tests/
npm run test

# 6. 提交代码
git add .
git commit -m "feat: 添加新功能"
git push
```

### 8.2 Claude 协作模式

```
你                              Claude
  │                                  │
  │  1. 描述需求                      │
  ├─────────────────────────────────>│
  │  "我需要一个用户注册接口"         │
  │                                  │
  │  2. Claude 分析并生成代码         │
  │<─────────────────────────────────┤
  │  [API 路由代码]                  │
  │  [Schema 验证模型]               │
  │  [数据库模型]                    │
  │                                  │
  │  3. Review 代码                   │
  │  ──────────────────────────────> │
  │                                  │
  │  4. 调整后运行测试                │
  │<─────────────────────────────────┤
  │  ✅ 测试通过                      │
  │                                  │
```

### 8.3 代码规范

#### Python (PEP 8)

```python
# ✅ 好的命名
class WeatherService:
    async def get_weather_data(self, city: str):
        pass

# ❌ 不好的命名
class WS:
    async def getData(self, c):
        pass
```

#### Vue 3

```vue
<!-- ✅ 好的组件结构 -->
<template>
  <div class="weather-card">
    <h2>{{ title }}</h2>
    <p>{{ temperature }}°C</p>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'

const props = defineProps<{
  title: string
  temperature: number
}>()
</script>

<style scoped>
.weather-card {
  padding: 16px;
}
</style>
```

---

## 9. 常见问题

### Q1: 为什么选择 PostgreSQL 而不是 MySQL？

**A:** PostgreSQL 在以下方面更优秀：

| 特性 | PostgreSQL | MySQL |
|------|------------|-------|
| JSON 支持 | 原生支持，功能强大 | 支持较弱 |
| 事务 | 完整 ACID 支持 | 部分场景较弱 |
| 性能 | 复杂查询更优秀 | 简单查询更快 |
| 扩展性 | 插件丰富 | 相对有限 |

### Q2: 前端为什么用 Vue 而不是 React？

**A:** 对你（非技术背景）来说：

| 对比维度 | Vue | React |
|----------|-----|-------|
| 学习难度 | ⭐⭐⭐ | ⭐⭐⭐⭐ |
| 中文文档 | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |
| 招聘市场 | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| Claude 支持 | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |

### Q3: 如何快速上手这个项目？

**A:** 按以下步骤：

1. **理解项目结构** - 阅读本技术文档
2. **运行项目** - 按照 README.md 启动
3. **阅读代码** - 从简单的接口开始（如 `weather.py`）
4. **修改功能** - 尝试修改一个小功能（如添加新的城市）
5. **让 Claude 帮助** - 遇到问题时直接问 Claude

### Q4: 需要多久能独立开发？

**A:** 估算时间：

| 阶段 | 时间 | 能达成 |
|------|------|--------|
| 理解基础概念 | 1-2 周 | 能看懂代码 |
| 修改现有功能 | 2-4 周 | 能独立改功能 |
| 开发新功能 | 1-2 月 | 能独立写功能 |
| 独立设计项目 | 3-6 月 | 能从零到一 |

### Q5: 如果遇到问题怎么办？

**A:** 解决优先级：

1. **问 Claude** - 最快，80% 问题能解决
2. **查文档** - 官方文档最准确
3. **搜社区** - Stack Overflow / 知乎
4. **找人帮忙** - 找技术合伙人/外包

---

## 📚 总结

这个示例项目展示了：

✅ **现代化技术栈** - Vue 3 + FastAPI + PostgreSQL
✅ **完整的架构** - 前后端分离、分层设计
✅ **生产级代码** - 类型安全、错误处理、测试
✅ **易于扩展** - 模块化设计、清晰的职责分离

**关键要点：**

1. **先理解，再动手** - 不要一开始就写代码
2. **从小功能开始** - 不要试图一次写完整个项目
3. **善用 Claude** - 它是你的编程助手
4. **多读代码** - 看懂别人的代码比自己写更重要

---

**有任何问题，随时问我！** 🚀
