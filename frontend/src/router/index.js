import { createRouter, createWebHistory } from 'vue-router'
import RegisterFormView from '../views/RegisterFormView.vue'
import LoginFormView from '../views/LoginFormView.vue'


const routes = [
  {
    path: '/register',
    name: 'register',
    component: RegisterFormView
  },
  {
    path: '/login',
    name: 'login',
    component: LoginFormView
  }

]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
