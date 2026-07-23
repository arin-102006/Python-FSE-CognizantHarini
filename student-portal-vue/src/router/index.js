import { createRouter, createWebHistory } from 'vue-router'
import CoursesView from '../views/CoursesView.vue'
import ProfileView from '../views/ProfileView.vue'
import CourseDetailView from '../views/CourseDetailView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      redirect: '/courses'
    },
    {
      path: '/courses',
      component: CoursesView
    },
    {
      path: '/courses/:id',
      component: CourseDetailView
    },
    {
      path: '/profile',
      component: ProfileView
    }
  ]
})

router.beforeEach((to, from, next) => {
  console.log('Navigating to:', to.path)
  next()
})

export default router