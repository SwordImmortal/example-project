<template>
  <a-config-provider :theme="{ token: { colorPrimary: '#1890ff' } }">
    <a-layout class="app-layout">
      <!-- 顶部导航 -->
      <a-layout-header class="header">
        <div class="logo">Example Project</div>
        <a-menu
          v-model:selectedKeys="selectedKeys"
          mode="horizontal"
          theme="dark"
          class="nav-menu"
        >
          <a-menu-item key="/">
            <home-outlined />
            首页
          </a-menu-item>
          <a-menu-item key="/weather">
            <cloud-outlined />
            天气
          </a-menu-item>
          <a-menu-item key="/news">
            <read-outlined />
            新闻
          </a-menu-item>
        </a-menu>
        <div class="user-info">
          <a-button v-if="!isLoggedIn" type="primary" @click="showLoginModal = true">
            登录
          </a-button>
          <a-dropdown v-else>
            <a-button>
              <user-outlined />
              {{ userStore.username }}
            </a-button>
            <template #overlay>
              <a-menu>
                <a-menu-item key="logout" @click="handleLogout">
                  退出登录
                </a-menu-item>
              </a-menu>
            </template>
          </a-dropdown>
        </div>
      </a-layout-header>

      <!-- 主内容区 -->
      <a-layout-content class="content">
        <router-view />
      </a-layout-content>

      <!-- 页脚 -->
      <a-layout-footer class="footer">
        Example Project © 2026 | 技术栈: Vue 3 + FastAPI + PostgreSQL
      </a-layout-footer>
    </a-layout>

    <!-- 登录弹窗 -->
    <a-modal
      v-model:open="showLoginModal"
      title="用户登录"
      @ok="handleLogin"
      @cancel="showLoginModal = false"
    >
      <a-form layout="vertical">
        <a-form-item label="用户名">
          <a-input v-model:value="loginForm.username" placeholder="请输入用户名" />
        </a-form-item>
        <a-form-item label="密码">
          <a-input-password v-model:value="loginForm.password" placeholder="请输入密码" />
        </a-form-item>
      </a-form>
    </a-modal>
  </a-config-provider>
</template>

<script setup lang="ts">
import { ref, computed, watch } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { message } from 'ant-design-vue'
import { useUserStore } from './stores/user'

const router = useRouter()
const route = useRoute()
const userStore = useUserStore()

// 选中的菜单项
const selectedKeys = ref<string[]>(['/'])

// 监听路由变化，更新选中菜单
watch(() => route.path, (path) => {
  selectedKeys.value = [path]
}, { immediate: true })

// 登录弹窗
const showLoginModal = ref(false)
const loginForm = ref({
  username: '',
  password: ''
})

// 是否已登录
const isLoggedIn = computed(() => userStore.isLoggedIn)

// 处理登录
const handleLogin = async () => {
  try {
    await userStore.login(loginForm.value)
    message.success('登录成功')
    showLoginModal.value = false
    loginForm.value = { username: '', password: '' }
  } catch (error) {
    message.error('登录失败，请检查用户名和密码')
  }
}

// 处理退出登录
const handleLogout = () => {
  userStore.logout()
  message.success('退出登录成功')
}
</script>

<style scoped>
.app-layout {
  min-height: 100vh;
}

.header {
  display: flex;
  align-items: center;
  padding: 0 24px;
  background: #001529;
}

.logo {
  color: white;
  font-size: 20px;
  font-weight: bold;
  margin-right: 48px;
}

.nav-menu {
  flex: 1;
  background: transparent;
  border-bottom: none;
}

.user-info {
  margin-left: 24px;
}

.content {
  padding: 24px;
  background: #f0f2f5;
  min-height: calc(100vh - 64px - 70px);
}

.footer {
  text-align: center;
  background: #f0f2f5;
}
</style>
