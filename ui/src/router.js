import Vue from 'vue';
import VueRouter from 'vue-router';
import Home from './Home.vue';
import Recipes from './Recipes.vue';
import Login from './Login.vue';
import store from './store';

const routes = [
  {
    path: '/',
    component: Home,
    name: 'home',
  },
  {
    path: '/recipes',
    component: Recipes,
    name: 'recipes',
  },
  {
    path: '/login',
    component: Login,
    name: 'login',

  },
];

Vue.use(VueRouter);
const router = new VueRouter({
  routes,
});

router.beforeEach((to, from, next) => {
  if (to.name !== 'login' && to.name !== 'home' && !store.state.user) {
    next({ name: 'login' });
  } else {
    next();
  }
});

export default router;
