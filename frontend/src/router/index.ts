import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/',
      name: 'Home',
      component: () => import('../views/Home.vue')
    },
    {
      path: '/weather',
      name: 'Weather',
      component: () => import('../views/Weather.vue')
    },
    {
      path: '/news',
      name: 'News',
      component: () => import('../views/News.vue')
    }
  ]
})

export default router
