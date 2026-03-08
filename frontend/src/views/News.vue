<template>
  <div class="news">
    <a-row :gutter="[24, 24]">
      <!-- 操作栏 -->
      <a-col :span="24">
        <a-card>
          <a-row :gutter="16" align="middle">
            <a-col :xs="24" :sm="12" :md="6">
              <a-select
                v-model:value="filters.category"
                placeholder="选择分类"
                style="width: 100%"
                allowClear
                @change="fetchNews"
              >
                <a-select-option value="科技">科技</a-select-option>
                <a-select-option value="AI">AI</a-select-option>
                <a-select-option value="编程">编程</a-select-option>
                <a-select-option value="生活">生活</a-select-option>
                <a-select-option value="健康">健康</a-select-option>
              </a-select>
            </a-col>
            <a-col :xs="24" :sm="12" :md="6">
              <a-select
                v-model:value="filters.source"
                placeholder="选择来源"
                style="width: 100%"
                allowClear
                @change="fetchNews"
              >
                <a-select-option value="Hacker News">Hacker News</a-select-option>
                <a-select-option value="GitHub Trending">GitHub Trending</a-select-option>
                <a-select-option value="36氪">36氪</a-select-option>
                <a-select-option value="腾讯科技">腾讯科技</a-select-option>
                <a-select-option value="新浪科技">新浪科技</a-select-option>
              </a-select>
            </a-col>
            <a-col :xs="24" :sm="12" :md="6">
              <a-button type="primary" :loading="loading" @click="fetchNews">
                <reload-outlined />
                刷新
              </a-button>
              <a-button
                type="default"
                :loading="scraping"
                @click="handleScrape"
                style="margin-left: 8px"
              >
                <cloud-download-outlined />
                抓取新闻
              </a-button>
            </a-col>
          </a-row>
        </a-card>
      </a-col>

      <!-- 新闻列表 -->
      <a-col :span="24">
        <a-card :loading="loading" title="新闻列表">
          <a-list
            :data-source="newsList"
            :pagination="pagination"
          >
            <template #renderItem="{ item }">
              <a-list-item>
                <a-list-item-meta>
                  <template #title>
                    <a :href="item.url" target="_blank">{{ item.title }}</a>
                  </template>
                  <template #description>
                    <a-space>
                      <a-tag color="blue">{{ item.category }}</a-tag>
                      <a-tag>{{ item.source }}</a-tag>
                      <span>{{ formatTime(item.created_at) }}</span>
                    </a-space>
                  </template>
                </a-list-item-meta>
                <template #actions>
                  <a-button
                    type="link"
                    size="small"
                    @click="showNewsDetail(item)"
                  >
                    详情
                  </a-button>
                </template>
              </a-list-item>
            </template>
          </a-list>

          <a-empty v-if="newsList.length === 0 && !loading" description="暂无新闻" />
        </a-card>
      </a-col>
    </a-row>

    <!-- 新闻详情弹窗 -->
    <a-modal
      v-model:open="detailVisible"
      title="新闻详情"
      width="800px"
      :footer="null"
    >
      <div v-if="currentNews">
        <h2>{{ currentNews.title }}</h2>
        <a-divider />
        <a-space style="margin-bottom: 16px">
          <a-tag color="blue">{{ currentNews.category }}</a-tag>
          <a-tag>{{ currentNews.source }}</a-tag>
          <span>{{ formatTime(currentNews.created_at) }}</span>
        </a-space>
        <p style="line-height: 1.8; white-space: pre-wrap;">
          {{ currentNews.content || '暂无内容' }}
        </p>
        <a-button v-if="currentNews.url" type="primary" :href="currentNews.url" target="_blank">
          查看原文
        </a-button>
      </div>
    </a-modal>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { message } from 'ant-design-vue'
import axios from 'axios'
import dayjs from 'dayjs'

interface NewsItem {
  id: number
  title: string
  content: string | null
  source: string | null
  category: string | null
  url: string | null
  created_at: string
}

// 加载状态
const loading = ref(false)
const scraping = ref(false)

// 筛选条件
const filters = ref({
  category: undefined,
  source: undefined
})

// 新闻列表
const newsList = ref<NewsItem[]>([])

// 分页
const pagination = ref({
  current: 1,
  pageSize: 10,
  total: 0
})

// 详情弹窗
const detailVisible = ref(false)
const currentNews = ref<NewsItem | null>(null)

// 获取新闻
const fetchNews = async () => {
  loading.value = true
  try {
    const params: any = { limit: 50 }
    if (filters.value.category) params.category = filters.value.category
    if (filters.value.source) params.source = filters.value.source

    const response = await axios.get('/api/v1/news/', { params })
    newsList.value = response.data.data
    pagination.value.total = response.data.data.length
  } catch (error) {
    message.error('获取新闻失败')
  } finally {
    loading.value = false
  }
}

// 抓取新闻
const handleScrape = async () => {
  scraping.value = true
  try {
    const category = filters.value.category || '科技'
    const response = await axios.post('/api/v1/news/scrape', {}, {
      params: { category }
    })
    message.success(response.data.message)
    // 刷新新闻列表
    await fetchNews()
  } catch (error) {
    message.error('抓取新闻失败')
  } finally {
    scraping.value = false
  }
}

// 显示新闻详情
const showNewsDetail = (news: NewsItem) => {
  currentNews.value = news
  detailVisible.value = true
}

// 格式化时间
const formatTime = (time: string) => {
  return dayjs(time).format('YYYY-MM-DD HH:mm')
}

// 初始化
onMounted(() => {
  fetchNews()
})
</script>

<style scoped>
.news {
  max-width: 1200px;
  margin: 0 auto;
}
</style>
