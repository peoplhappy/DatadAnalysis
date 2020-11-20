import Vue from 'vue'
import Router from 'vue-router'
import datasheet from '@/components/datasheet'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'datasheet',
      component: datasheet
    }
  ]
})
