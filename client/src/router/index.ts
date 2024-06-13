import { createRouter, createWebHistory } from 'vue-router'
import PingComponent from '@/components/PingComponent.vue'
import BooksComponent from '@/components/BooksComponent.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/books',
      name: 'Books',
      component: BooksComponent
    },
    {
      path: '/',
      name: 'Ping',
      component: PingComponent
    }
  ]
})

export default router
