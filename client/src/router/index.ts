import { createRouter, createWebHistory } from 'vue-router'
import PingComponent from '../components/PingComponent.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/Ping',
      name: 'ping',
      component: PingComponent
    }
  ]
})

export default router
