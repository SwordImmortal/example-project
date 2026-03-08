<template>
  <div class="home">
    <a-row :gutter="[24, 24]">
      <!-- 欢迎卡片 -->
      <a-col :span="24">
        <a-card class="welcome-card">
          <h1>👋 欢迎来到示例项目</h1>
          <p>这是一个现代化的 Web 应用示例，采用前后端分离架构。</p>
          <p class="tech-stack">
            技术栈：Vue 3 + TypeScript + Vite + FastAPI + PostgreSQL
          </p>
          <a-space>
            <a-button type="primary" size="large" @click="router.push('/weather')">
              查看天气
            </a-button>
            <a-button size="large" @click="router.push('/news')">
              浏览新闻
            </a-button>
          </a-space>
        </a-card>
      </a-col>

      <!-- 功能介绍 -->
      <a-col :xs="24" :sm="12" :md="8">
        <a-card hoverable class="feature-card">
          <template #cover>
            <div class="feature-icon">🌤️</div>
          </template>
          <a-card-meta title="天气查询">
            <template #description>
              实时查询多城市天气信息，支持历史天气查询和天气订阅。
            </template>
          </a-card-meta>
        </a-card>
      </a-col>

      <a-col :xs="24" :sm="12" :md="8">
        <a-card hoverable class="feature-card">
          <template #cover>
            <div class="feature-icon">📰</div>
          </template>
          <a-card-meta title="新闻推送">
            <template #description>
              获取最新科技新闻，支持分类筛选和来源过滤。
            </template>
          </a-card-meta>
        </a-card>
      </a-col>

      <a-col :xs="24" :sm="12" :md="8">
        <a-card hoverable class="feature-card">
          <template #cover>
            <div class="feature-icon">👤</div>
          </template>
          <a-card-meta title="用户管理">
            <template #description>
              完整的用户认证系统，支持注册、登录和用户信息管理。
            </template>
          </a-card-meta>
        </a-card>
      </a-col>

      <!-- 技术特性 -->
      <a-col :span="24">
        <a-card title="技术特性" class="features-list">
          <a-row :gutter="16">
            <a-col :xs="24" :sm="12" :md="6">
              <div class="feature-item">
                <check-circle-outlined class="feature-check" />
                <span>前后端分离架构</span>
              </div>
            </a-col>
            <a-col :xs="24" :sm="12" :md="6">
              <div class="feature-item">
                <check-circle-outlined class="feature-check" />
                <span>RESTful API</span>
              </div>
            </a-col>
            <a-col :xs="24" :sm="12" :md="6">
              <div class="feature-item">
                <check-circle-outlined class="feature-check" />
                <span>TypeScript 类型安全</span>
              </div>
            </a-col>
            <a-col :xs="24" :sm="12" :md="6">
              <div class="feature-item">
                <check-circle-outlined class="feature-check" />
                <span>响应式设计</span>
              </div>
            </a-col>
            <a-col :xs="24" :sm="12" :md="6">
              <div class="feature-item">
                <check-circle-outlined class="feature-check" />
                <span>JWT 认证</span>
              </div>
            </a-col>
            <a-col :xs="24" :sm="12" :md="6">
              <div class="feature-item">
                <check-circle-outlined class="feature-check" />
                <span>PostgreSQL 数据库</span>
              </div>
            </a-col>
            <a-col :xs="24" :sm="12" :md="6">
              <div class="feature-item">
                <check-circle-outlined class="feature-check" />
                <span>Redis 缓存</span>
              </div>
            </a-col>
            <a-col :xs="24" :sm="12" :md="6">
              <div class="feature-item">
                <check-circle-outlined class="feature-check" />
                <span>Docker 部署</span>
              </div>
            </a-col>
          </a-row>
        </a-card>
      </a-col>
    </a-row>
  </div>
</template>

<script setup lang="ts">
import { useRouter } from 'vue-router'

const router = useRouter()
</script>

<style scoped>
.home {
  max-width: 1200px;
  margin: 0 auto;
}

.welcome-card {
  text-align: center;
  padding: 40px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}

.welcome-card h1 {
  color: white;
  font-size: 36px;
  margin-bottom: 16px;
}

.welcome-card p {
  color: rgba(255, 255, 255, 0.9);
  font-size: 16px;
  margin-bottom: 24px;
}

.tech-stack {
  color: rgba(255, 255, 255, 0.8);
  font-size: 14px;
}

.feature-card {
  text-align: center;
  height: 100%;
}

.feature-icon {
  font-size: 64px;
  padding: 40px;
  background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
}

.features-list {
  margin-top: 24px;
}

.feature-item {
  display: flex;
  align-items: center;
  padding: 12px 0;
}

.feature-check {
  color: #52c41a;
  font-size: 20px;
  margin-right: 8px;
}
</style>
