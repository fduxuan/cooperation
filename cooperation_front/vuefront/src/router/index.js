import Vue from 'vue'
import Router from 'vue-router'


Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'cornerstone',
      component: () => import('@/view/Login.vue')
    },
    {
      path: '/loginconfirm',
      name: 'loginconfirm',
      component: () => import('@/view/LoginConfirm.vue')
    },
    {
      path: '/square',
      name: 'square',
      component: () => import('@/view/Square.vue')
    },
    {
      path: '/auth',
      name: 'auth',
      component: () => import('@/view/Auth.vue')
    },
    {
      path:'/myindex',
      name:'myindex',
      component: () => import('@/view/MyInfo/MyIndex.vue')
    },
    {
      path:'/mynotification',
      name:'mynotification',
      component: () => import('@/view/MyInfo/MyNotification.vue')
    },
    {
      path:'/mymodify',
      name:'mymodify',
      component: () => import('@/view/MyInfo/MyModify.vue')
    },
    {
      path:'/mymodifydetail',
      name:'mymodifydetail',
      component: () => import('@/view/MyInfo/MyModifyDetail.vue')
    },
    {
      path: '/myfriend',
      name: 'myfriend',
      component: () => import('@/view/MyInfo/MyFriend.vue')
    },
    {
      path: '/mydocument',
      name: 'mydocument',
      component: () => import('@/view/MyInfo/MyDocument.vue')
    },
    {
      path: '/mypet',
      name: 'mypet',
      component: () => import('@/view/MyInfo/MyPet.vue')
    },
    {
      path: '/about',
      name: 'about',
      component: () => import('@/view/MyInfo/About.vue')
    },
    {
      path: '/about2',
      name: 'about2',
      component: () => import('@/view/MyInfo/About2.vue')
    },
    {
      path: '/about3',
      name: 'about3',
      component: () => import('@/view/MyInfo/About3.vue')
    },
    {
      path:'/task',
      name:'task',
      component: () => import('@/view/Task/Task.vue')
    },
    {
      path:'/taskdetail/:tid',
      name:'taskdetail',
      component: () => import('@/view/Task/TaskDetail.vue')
    },
    {
      path: '/plandetail/:pid',
      name: 'plandetail',
      component: () => import('@/view/Plan/PlanDetail.vue')
    },

  ]
})
