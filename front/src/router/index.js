import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: () => import('@/pages/home/HomePage.vue'),
  },
  {
    path: '/match',
    name: 'Match',
    component: () => import('@/pages/match/MatchPage.vue'),
  },
  {
    path: '/results',
    name: 'Results',
    component: () => import('@/pages/results/ResultsPage.vue'),
  },
  {
    path: '/signUp',
    name: 'SignUp',
    component: () => import('@/pages/signUp/SignUpPage.vue'),
  },
  {
    path: '/logIn',
    name: 'LogIn',
    component: () => import('@/pages/logIn/LogInPage.vue'),
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
})

export default router
