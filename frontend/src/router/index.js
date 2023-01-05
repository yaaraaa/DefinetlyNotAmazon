import { createRouter, createWebHistory } from 'vue-router'

import HomeView from '../views/HomeView.vue'
import AddItemView from '../views/AddItemView.vue'
import UpdateItemView from '../views/UpdateItemView.vue'
import DeleteItem from '../views/DeleteItem.vue'
import ViewItems from '../views/ViewItems.vue'


const routes = [
  {
    path: '/',
    name: 'homeView',
    component: HomeView
  },
  {
    path: '/add-product',
    name: 'addProduct',
    component: AddItemView
  },
  {
    path: '/update-product',
    name: 'updateProduct',
    component: UpdateItemView
  },
  {
    path: '/delete-product',
    name: 'deleteProduct',
    component: DeleteItem
  },
  {
    path: '/View-products',
    name: 'viewProduct',
    component: ViewItems
  }          

]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
