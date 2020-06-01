import Vue from 'vue';
import App from './App.vue';
import store from './store';
import router from './router';

import axios from 'axios';
const authHeader = 'Token ' + localStorage.getItem('jwtToken');
axios.defaults.headers.common['Authorization'] = authHeader;

import './styles/colors.css';

Vue.config.productionTip = false;

new Vue({
  router,
  store,
  render: h => h(App),
}).$mount('#app');
