import Vue from 'vue';
import VueRouter from 'vue-router';
import App from './App.vue';
import Home from './Home.vue';
import Recipes from './Recipes.vue';
import Login from './Login.vue';


import axios from 'axios';
const authHeader = 'Token ' + localStorage.getItem('jwtToken');
axios.defaults.headers.common['Authorization'] = authHeader;

import './styles/colors.css';


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

Vue.config.productionTip = false;

new Vue({
  router,
  render: h => h(App),
}).$mount('#app');
