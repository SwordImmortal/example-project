<template>
  <div class="weather">
    <a-row :gutter="[24, 24]">
      <!-- 天气查询 -->
      <a-col :span="24">
        <a-card title="天气查询">
          <a-form layout="inline" @submit="handleSearch">
            <a-form-item label="城市">
              <a-input
                v-model:value="searchForm.city"
                placeholder="请输入城市名称"
                style="width: 200px"
                @pressEnter="handleSearch"
              />
            </a-form-item>
            <a-form-item>
              <a-button type="primary" :loading="loading" @click="handleSearch">
                <search-outlined />
                查询
              </a-button>
            </a-form-item>
          </a-form>
        </a-card>
      </a-col>

      <!-- 当前天气 -->
      <a-col :xs="24" :md="12">
        <a-card :loading="loading" title="当前天气">
          <div v-if="weather" class="current-weather">
            <div class="weather-main">
              <div class="weather-icon">{{ getWeatherIcon(weather.description) }}</div>
              <div class="weather-info">
                <h2>{{ weather.city }}</h2>
                <p class="temperature">{{ weather.temperature }}°C</p>
                <p class="description">{{ weather.description }}</p>
              </div>
            </div>
            <a-divider />
            <a-row :gutter="16">
              <a-col :span="12">
                <div class="weather-detail">
                  <drop-outlined />
                  <span>湿度: {{ weather.humidity }}%</span>
                </div>
              </a-col>
              <a-col :span="12">
                <div class="weather-detail">
                  <clock-circle-outlined />
                  <span>更新: {{ formatTime(weather.created_at) }}</span>
                </div>
              </a-col>
            </a-row>
          </div>
          <a-empty v-else description="请输入城市查询天气" />
        </a-card>
      </a-col>

      <!-- 历史天气 -->
      <a-col :xs="24" :md="12">
        <a-card :loading="historyLoading" title="历史天气">
          <div v-if="weatherHistory">
            <a-statistic
              title="平均温度"
              :value="weatherHistory.avg_temperature"
              suffix="°C"
              :precision="1"
              style="margin-bottom: 24px"
            />
            <a-list
              :data-source="weatherHistory.records"
              size="small"
              :pagination="false"
            >
              <template #renderItem="{ item }">
                <a-list-item>
                  <a-list-item-meta>
                    <template #title>
                      <span>{{ item.city }}</span>
                    </template>
                    <template #description>
                      {{ formatTime(item.created_at) }}
                    </template>
                  </a-list-item-meta>
                  <template #actions>
                    <span class="weather-action">
                      {{ item.temperature }}°C - {{ item.description }}
                    </span>
                  </template>
                </a-list-item>
              </template>
            </a-list>
          </div>
          <a-empty v-else description="暂无历史数据" />
        </a-card>
      </a-col>
    </a-row>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { message } from 'ant-design-vue'
import axios from 'axios'
import dayjs from 'dayjs'

interface WeatherData {
  id: number
  city: string
  temperature: number
  humidity: number
  description: string
  created_at: string
}

interface WeatherHistory {
  city: string
  avg_temperature: number | null
  records: WeatherData[]
}

// 搜索表单
const searchForm = ref({ city: '' })

// 加载状态
const loading = ref(false)
const historyLoading = ref(false)

// 天气数据
const weather = ref<WeatherData | null>(null)
const weatherHistory = ref<WeatherHistory | null>(null)

// 查询天气
const handleSearch = async () => {
  if (!searchForm.value.city) {
    message.warning('请输入城市名称')
    return
  }

  loading.value = true
  try {
    const response = await axios.get(`/api/v1/weather/${searchForm.value.city}`)
    weather.value = response.data.data

    // 同时查询历史天气
    await fetchWeatherHistory(searchForm.value.city)
  } catch (error) {
    message.error('查询天气失败')
  } finally {
    loading.value = false
  }
}

// 查询历史天气
const fetchWeatherHistory = async (city: string) => {
  historyLoading.value = true
  try {
    const response = await axios.get(`/api/v1/weather/history/${city}?days=7`)
    weatherHistory.value = response.data.data
  } catch (error) {
    message.error('查询历史天气失败')
  } finally {
    historyLoading.value = false
  }
}

// 获取天气图标
const getWeatherIcon = (description: string) => {
  const icons: Record<string, string> = {
    '晴': '☀️',
    '多云': '⛅',
    '阴': '☁️',
    '小雨': '🌦️',
    '中雨': '🌧️',
    '大雨': '🌧️',
    '雷阵雨': '⛈️'
  }
  return icons[description] || '🌡️'
}

// 格式化时间
const formatTime = (time: string) => {
  return dayjs(time).format('YYYY-MM-DD HH:mm')
}
</script>

<style scoped>
.weather {
  max-width: 1200px;
  margin: 0 auto;
}

.current-weather {
  padding: 20px 0;
}

.weather-main {
  display: flex;
  align-items: center;
  gap: 24px;
}

.weather-icon {
  font-size: 64px;
}

.weather-info h2 {
  font-size: 32px;
  margin-bottom: 8px;
}

.temperature {
  font-size: 48px;
  font-weight: bold;
  color: #1890ff;
  margin: 0;
}

.description {
  font-size: 20px;
  color: #666;
  margin: 0;
}

.weather-detail {
  display: flex;
  align-items: center;
  gap: 8px;
  color: #666;
}

.weather-action {
  color: #1890ff;
}
</style>
