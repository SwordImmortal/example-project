# 示例项目 - 现代化 Web 应用

一个完整的现代化 Web 应用示例，包含用户管理、天气查询、新闻推送等功能。

## 📋 项目概览

- **项目名称**：Example Project
- **创建时间**：2026-03-08
- **技术栈**：Vue 3 + FastAPI + PostgreSQL
- **用途**：学习现代化 Web 开发架构

---

## 🏗️ 技术架构

### 架构图

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
│  │                    业务逻辑层                         │   │
│  │  ┌─────────┐  ┌─────────┐  ┌─────────┐             │   │
│  │  │ UserService│ WeatherService │ NewsService│       │   │
│  │  └─────────┘  └─────────┘  └─────────┘             │   │
│  └───────────────────────┬─────────────────────────────┘   │
│                         ▼                                  │
│  ┌─────────────────────────────────────────────────────┐   │
│  │                    数据访问层                         │   │
│  │  ┌─────────┐  ┌─────────┐  ┌─────────┐             │   │
│  │  │   Models │  │ Schemas │  │  CRUD   │             │   │
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

---

## 🎯 核心特性

- ✅ 用户注册/登录
- ✅ 天气查询（支持多城市）
- ✅ 新闻推送（定时任务）
- ✅ 数据可视化
- ✅ 响应式设计
- ✅ RESTful API
- ✅ 自动化测试
- ✅ Docker 部署

---

## 🚀 快速开始

### 1. 克隆项目

```bash
cd D:\coding\example-project
```

### 2. 启动数据库

```bash
docker-compose up -d
```

### 3. 启动后端

```bash
cd backend
pip install -r requirements.txt
python main.py
```

### 4. 启动前端

```bash
cd frontend
npm install
npm run dev
```

### 5. 访问应用

- 前端：http://localhost:5173
- 后端 API：http://localhost:8000
- API 文档：http://localhost:8000/docs

---

## 📁 项目结构

```
D:\coding\example-project/
├── frontend/                  # 前端项目（Vue 3）
│   ├── src/
│   │   ├── api/              # API 调用
│   │   ├── components/       # 可复用组件
│   │   ├── views/            # 页面组件
│   │   ├── stores/           # 状态管理（Pinia）
│   │   ├── utils/            # 工具函数
│   │   ├── App.vue           # 根组件
│   │   └── main.ts           # 入口文件
│   ├── package.json
│   ├── vite.config.ts
│   └── tsconfig.json
│
├── backend/                   # 后端项目（FastAPI）
│   ├── app/
│   │   ├── api/              # API 路由
│   │   │   ├── users.py
│   │   │   ├── weather.py
│   │   │   └── news.py
│   │   ├── core/             # 核心配置
│   │   │   ├── config.py
│   │   │   ├── security.py
│   │   │   └── database.py
│   │   ├── models/           # 数据库模型
│   │   │   ├── user.py
│   │   │   ├── weather.py
│   │   │   └── news.py
│   │   ├── schemas/          # Pydantic 模型
│   │   ├── services/         # 业务逻辑
│   │   └── utils/            # 工具函数
│   ├── alembic/              # 数据库迁移
│   ├── tests/                # 测试
│   ├── main.py               # 应用入口
│   └── requirements.txt
│
├── docker-compose.yml         # Docker 配置
├── .env.example              # 环境变量示例
├── TECHNICAL_GUIDE.md        # 技术说明文档
└── README.md                 # 项目说明
```

---

## 🔧 技术栈详解

### 前端技术栈

| 技术 | 版本 | 用途 |
|------|------|------|
| Vue 3 | 3.4+ | 前端框架 |
| TypeScript | 5.3+ | 类型安全 |
| Vite | 5.0+ | 构建工具 |
| Pinia | 2.1+ | 状态管理 |
| Ant Design Vue | 4.1+ | UI 组件库 |
| Axios | 1.6+ | HTTP 客户端 |

### 后端技术栈

| 技术 | 版本 | 用途 |
|------|------|------|
| FastAPI | 0.109+ | Web 框架 |
| SQLAlchemy | 2.0+ | ORM |
| Alembic | 1.13+ | 数据库迁移 |
| Pydantic | 2.5+ | 数据验证 |
| Uvicorn | 0.27+ | ASGI 服务器 |
| Redis-py | 5.0+ | Redis 客户端 |

### 数据库

| 技术 | 版本 | 用途 |
|------|------|------|
| PostgreSQL | 16+ | 主数据库 |
| Redis | 7+ | 缓存 |

---

## 📊 数据库设计

### 用户表 (users)

| 字段 | 类型 | 说明 |
|------|------|------|
| id | INTEGER | 主键 |
| username | VARCHAR(50) | 用户名（唯一） |
| email | VARCHAR(100) | 邮箱（唯一） |
| hashed_password | VARCHAR(255) | 加密密码 |
| created_at | TIMESTAMP | 创建时间 |
| updated_at | TIMESTAMP | 更新时间 |

### 天气表 (weather_records)

| 字段 | 类型 | 说明 |
|------|------|------|
| id | INTEGER | 主键 |
| city | VARCHAR(50) | 城市 |
| temperature | INTEGER | 温度 |
| humidity | INTEGER | 湿度 |
| description | VARCHAR(100) | 天气描述 |
| created_at | TIMESTAMP | 记录时间 |

### 新闻表 (news_records)

| 字段 | 类型 | 说明 |
|------|------|------|
| id | INTEGER | 主键 |
| title | VARCHAR(255) | 标题 |
| content | TEXT | 内容 |
| source | VARCHAR(50) | 来源 |
| category | VARCHAR(50) | 分类 |
| url | VARCHAR(500) | 链接 |
| created_at | TIMESTAMP | 创建时间 |

---

## 🔌 API 接口

### 用户接口

| 方法 | 路径 | 说明 |
|------|------|------|
| POST | /api/v1/users/register | 用户注册 |
| POST | /api/v1/users/login | 用户登录 |
| GET | /api/v1/users/me | 获取当前用户信息 |
| PUT | /api/v1/users/me | 更新用户信息 |

### 天气接口

| 方法 | 路径 | 说明 |
|------|------|------|
| GET | /api/v1/weather/{city} | 获取城市天气 |
| GET | /api/v1/weather/history/{city} | 获取历史天气 |
| POST | /api/v1/weather/subscribe | 订阅城市天气 |

### 新闻接口

| 方法 | 路径 | 说明 |
|------|------|------|
| GET | /api/v1/news | 获取新闻列表 |
| GET | /api/v1/news/{id} | 获取新闻详情 |
| POST | /api/v1/news/scrape | 抓取新闻 |

---

## 🧪 测试

### 后端测试

```bash
cd backend
pytest tests/
```

### 前端测试

```bash
cd frontend
npm run test
```

---

## 📦 部署

### Docker 部署

```bash
docker-compose up -d
```

### 云部署

- **前端**：Vercel / Netlify
- **后端**：Railway / Render / 阿里云
- **数据库**：Supabase / 阿里云 RDS

---

## 📚 文档

- [技术说明文档](./TECHNICAL_GUIDE.md) - 详细的技术架构说明
- [API 文档](http://localhost:8000/docs) - 自动生成的 Swagger 文档

---

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

---

## 📄 许可证

MIT License
