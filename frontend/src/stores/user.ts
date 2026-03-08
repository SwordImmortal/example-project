import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import axios from 'axios'

interface LoginForm {
  username: string
  password: string
}

interface UserInfo {
  id: number
  username: string
  email: string
}

export const useUserStore = defineStore('user', () => {
  // Token
  const token = ref<string>(localStorage.getItem('token') || '')
  const userInfo = ref<UserInfo | null>(null)

  // 是否已登录
  const isLoggedIn = computed(() => !!token.value)
  const username = computed(() => userInfo.value?.username || '游客')

  // 登录
  const login = async (form: LoginForm) => {
    const formData = new FormData()
    formData.append('username', form.username)
    formData.append('password', form.password)

    const response = await axios.post('/api/v1/users/login', formData)
    const { data } = response.data.data

    // 保存 token
    token.value = data.access_token
    localStorage.setItem('token', data.access_token)

    // 获取用户信息
    await fetchUserInfo()
  }

  // 获取用户信息
  const fetchUserInfo = async () => {
    const response = await axios.get('/api/v1/users/me', {
      headers: { Authorization: `Bearer ${token.value}` }
    })
    userInfo.value = response.data.data
  }

  // 退出登录
  const logout = () => {
    token.value = ''
    userInfo.value = null
    localStorage.removeItem('token')
  }

  return {
    token,
    userInfo,
    isLoggedIn,
    username,
    login,
    fetchUserInfo,
    logout
  }
})
