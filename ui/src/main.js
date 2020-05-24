import Vue from 'vue';
import VueRouter from 'vue-router';
import App from './App.vue';
import Home from './Home.vue';
import Recipes from './Recipes.vue';
import RecipeCreate from './RecipeCreate.vue';

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
    path: '/recipes/create',
    component: RecipeCreate,
    name: 'recipe-create',
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
