# Example Project - 现代化 Web 应用

[![Vue 3](https://img.shields.io/badge/Vue-3.4+-4FC08D?logo=vue.js)](https://vuejs.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.109+-009688?logo=fastapi)](https://fastapi.tiangolo.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16+-336791?logo=postgresql)](https://www.postgresql.org/)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

一个完整的现代化全栈 Web 应用示例，采用 Vue 3 + FastAPI + PostgreSQL 技术栈，包含用户管理、天气查询、新闻推送等功能模块。

> 📌 **项目状态**：开发中 | 核心功能已完成，部分模块待完善

---

## 目录

- [项目概览](#项目概览)
- [技术架构](#技术架构)
- [快速开始](#快速开始)
- [项目结构](#项目结构)
- [API 文档](#api-文档)
- [数据库设计](#数据库设计)
- [开发指南](#开发指南)
- [部署说明](#部署说明)

---

## 项目概览

| 项目 | 信息 |
|------|------|
| **名称** | Example Project |
| **仓库** | https://github.com/SwordImmortal/example-project |
| **创建时间** | 2026-03-08 |
| **技术栈** | Vue 3 + TypeScript + FastAPI + PostgreSQL |
| **用途** | 现代化全栈开发架构学习与参考 |

### 核心特性

- 🔐 **用户系统** - 注册、登录、JWT 认证
- 🌤️ **天气查询** - 多城市天气实时查询与历史记录
- 📰 **新闻推送** - 新闻抓取与分类展示
- 📊 **数据可视化** - 天气数据图表展示
- 📱 **响应式设计** - 适配多端设备
- 🐳 **Docker 支持** - 一键部署

---

## 技术架构

```
┌─────────────────────────────────────────────────────────────┐
│                         用户浏览器                           │
│  ┌─────────────────────────────────────────────────────┐   │
│  │                    前端 (Vue 3)                      │   │
│  │  ┌─────────┐  ┌─────────┐  ┌─────────┐             │   │
│  │  │ Components │  │  Views   │  │  Stores  │             │   │
│  │  └─────────┘  └─────────┘  └─────────┘             │   │
│  └─────────────────────────────────────────────────────┘   │
└───────────────────────┬─────────────────────────────────────┘
                        │ HTTP/JSON
                        ▼
┌─────────────────────────────────────────────────────────────┐
│                    后端 (FastAPI)                            │
│  ┌─────────────────────────────────────────────────────┐   │
│  │                    API 路由层                         │   │
│  │  ┌─────────┐  ┌─────────┐  ┌─────────┐             │   │
│  │  │ users   │  │ weather │  │  news   │             │   │
│  │  └─────────┘  └─────────┘  └─────────┘             │   │
│  └───────────────────────┬─────────────────────────────┘   │
│                         ▼                                  │
│  ┌─────────────────────────────────────────────────────┐   │
│  │                    数据访问层                         │   │
│  │  ┌─────────┐  ┌─────────┐  ┌─────────┐             │   │
│  │  │  Models  │  │ Schemas │  │  CRUD   │             │   │
│  │  └─────────┘  └─────────┘  └─────────┘             │   │
│  └─────────────────────────────────────────────────────┘   │
└───────────────────────┬─────────────────────────────────────┘
                        │
        ┌───────────────┼───────────────┐
        ▼               ▼               ▼
┌──────────────┐  ┌──────────┐  ┌──────────────┐
│ PostgreSQL   │  │  Redis   │  │ 外部 API     │
│  (主数据库)   │  │  (缓存)   │  │ (天气/新闻)  │
└──────────────┘  └──────────┘  └──────────────┘
```

### 技术栈版本

| 层级 | 技术 | 版本 | 说明 |
|------|------|------|------|
| 前端框架 | Vue 3 | 3.4+ | Composition API |
| 类型系统 | TypeScript | 5.3+ | 类型安全 |
| 构建工具 | Vite | 5.0+ | 快速开发构建 |
| 状态管理 | Pinia | 2.1+ | 轻量级状态管理 |
| UI 组件 | Ant Design Vue | 4.1+ | 企业级组件库 |
| HTTP 客户端 | Axios | 1.6+ | 请求封装 |
| 后端框架 | FastAPI | 0.109+ | 高性能异步框架 |
| ORM | SQLAlchemy | 2.0+ | 异步 ORM |
| 数据验证 | Pydantic | 2.5+ | 数据模型验证 |
| 数据库 | PostgreSQL | 16+ | 主数据库 |
| 缓存 | Redis | 7+ | 缓存与会话存储 |

---

## 快速开始

### 环境要求

- Node.js 18+
- Python 3.11+
- PostgreSQL 16+
- Redis 7+ (可选)
- Docker & Docker Compose (推荐)

### 安装步骤

```bash
# 1. 克隆项目
git clone https://github.com/SwordImmortal/example-project.git
cd example-project

# 2. 复制环境变量配置
cp .env.example .env
# 编辑 .env 文件，配置数据库连接信息

# 3. 启动数据库 (Docker)
docker-compose up -d

# 4. 启动后端
cd backend
pip install -r requirements.txt
python main.py

# 5. 启动前端 (新终端)
cd frontend
npm install
npm run dev
```

### 访问地址

| 服务 | 地址 | 说明 |
|------|------|------|
| 前端应用 | http://localhost:5173 | Vue 开发服务器 |
| 后端 API | http://localhost:8000 | FastAPI 服务 |
| API 文档 | http://localhost:8000/docs | Swagger UI |
| API 文档 | http://localhost:8000/redoc | ReDoc |

---

## 项目结构

```
example-project/
├── frontend/                    # 前端项目
│   ├── src/
│   │   ├── api/                # API 请求封装
│   │   ├── components/         # 公共组件
│   │   ├── views/              # 页面组件
│   │   │   ├── Home.vue        # 首页
│   │   │   ├── Weather.vue     # 天气页
│   │   │   └── News.vue        # 新闻页
│   │   ├── stores/             # Pinia 状态管理
│   │   ├── router/             # 路由配置
│   │   ├── utils/              # 工具函数
│   │   ├── App.vue             # 根组件
│   │   └── main.ts             # 入口文件
│   ├── package.json
│   └── vite.config.ts
│
├── backend/                     # 后端项目
│   ├── app/
│   │   ├── api/                # API 路由
│   │   │   ├── users.py        # 用户接口
│   │   │   ├── weather.py      # 天气接口
│   │   │   └── news.py         # 新闻接口
│   │   ├── core/               # 核心配置
│   │   │   ├── config.py       # 应用配置
│   │   │   ├── database.py     # 数据库连接
│   │   │   └── security.py     # 安全认证
│   │   ├── models/             # 数据库模型
│   │   ├── schemas/            # Pydantic 模型
│   │   ├── services/           # 业务逻辑
│   │   └── utils/              # 工具函数
│   ├── alembic/                # 数据库迁移
│   ├── tests/                  # 测试用例
│   ├── main.py                 # 应用入口
│   └── requirements.txt        # Python 依赖
│
├── docker-compose.yml           # Docker 编排
├── .env.example                # 环境变量模板
├── TECHNICAL_GUIDE.md          # 技术详解
└── README.md                   # 项目说明
```

---

## API 文档

### 用户模块 `/api/v1/users`

| 方法 | 路径 | 说明 | 认证 |
|------|------|------|------|
| POST | /register | 用户注册 | ❌ |
| POST | /login | 用户登录 | ❌ |
| GET | /me | 获取当前用户 | ✅ |
| PUT | /me | 更新用户信息 | ✅ |

### 天气模块 `/api/v1/weather`

| 方法 | 路径 | 说明 | 认证 |
|------|------|------|------|
| GET | /{city} | 获取城市天气 | ❌ |
| GET | /history/{city} | 获取历史天气 | ❌ |
| POST | /subscribe | 订阅天气推送 | ✅ |

### 新闻模块 `/api/v1/news`

| 方法 | 路径 | 说明 | 认证 |
|------|------|------|------|
| GET | / | 获取新闻列表 | ❌ |
| GET | /{id} | 获取新闻详情 | ❌ |
| POST | /scrape | 抓取最新新闻 | ✅ |

> 完整 API 文档请访问 http://localhost:8000/docs

---

## 数据库设计

### 用户表 (users)

| 字段 | 类型 | 约束 | 说明 |
|------|------|------|------|
| id | INTEGER | PK, AUTO | 主键 |
| username | VARCHAR(50) | UNIQUE, NOT NULL | 用户名 |
| email | VARCHAR(100) | UNIQUE, NOT NULL | 邮箱 |
| hashed_password | VARCHAR(255) | NOT NULL | 加密密码 |
| created_at | TIMESTAMP | DEFAULT NOW | 创建时间 |
| updated_at | TIMESTAMP | | 更新时间 |

### 天气记录表 (weather_records)

| 字段 | 类型 | 约束 | 说明 |
|------|------|------|------|
| id | INTEGER | PK, AUTO | 主键 |
| city | VARCHAR(50) | NOT NULL | 城市名 |
| temperature | INTEGER | | 温度 (°C) |
| humidity | INTEGER | | 湿度 (%) |
| description | VARCHAR(100) | | 天气描述 |
| created_at | TIMESTAMP | DEFAULT NOW | 记录时间 |

### 新闻表 (news_records)

| 字段 | 类型 | 约束 | 说明 |
|------|------|------|------|
| id | INTEGER | PK, AUTO | 主键 |
| title | VARCHAR(255) | NOT NULL | 标题 |
| content | TEXT | | 内容 |
| source | VARCHAR(50) | | 来源 |
| category | VARCHAR(50) | | 分类 |
| url | VARCHAR(500) | | 原文链接 |
| created_at | TIMESTAMP | DEFAULT NOW | 创建时间 |

---

## 开发指南

### 常用命令

```bash
# 前端开发
cd frontend
npm run dev          # 启动开发服务器
npm run build        # 构建生产版本
npm run preview      # 预览生产构建

# 后端开发
cd backend
python main.py                    # 启动开发服务器
alembic revision --autogenerate -m "描述"  # 生成迁移
alembic upgrade head              # 执行迁移
pytest tests/                     # 运行测试

# Docker
docker-compose up -d              # 启动所有服务
docker-compose down               # 停止所有服务
docker-compose logs -f            # 查看日志
```

### 开发进度

| 模块 | 状态 | 说明 |
|------|------|------|
| 用户认证 | ✅ 完成 | 注册、登录、JWT |
| 天气模块 | ✅ 完成 | 查询、历史记录 |
| 新闻模块 | ✅ 完成 | 列表、详情、抓取 |
| 前端页面 | ✅ 完成 | Home、Weather、News |
| 单元测试 | 🚧 进行中 | 待补充测试用例 |
| Docker 部署 | ✅ 完成 | docker-compose 配置 |

---

## 部署说明

### Docker 部署（推荐）

```bash
# 构建并启动
docker-compose up -d --build

# 查看状态
docker-compose ps

# 查看日志
docker-compose logs -f
```

### 云平台部署

| 组件 | 推荐平台 | 说明 |
|------|----------|------|
| 前端 | Vercel / Netlify | 静态站点托管 |
| 后端 | Railway / Render | 容器化部署 |
| 数据库 | Supabase / Neon | 托管 PostgreSQL |
| 缓存 | Upstash | 托管 Redis |

---

## 相关文档

- [技术详解](./TECHNICAL_GUIDE.md) - 深入的技术架构说明
- [API 文档](http://localhost:8000/docs) - 交互式 API 文档

---

## 许可证

[MIT License](LICENSE)

---

## 贡献

欢迎提交 Issue 和 Pull Request！

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 提交 Pull Request
