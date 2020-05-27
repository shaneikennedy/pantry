import Vue from 'vue';
import VueRouter from 'vue-router';
import App from './App.vue';


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
