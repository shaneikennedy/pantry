import Vue from "vue";
import axios from "axios";

import App from "./App.vue";
import store from "./store";
import router from "./router";

const tokenData = JSON.parse(localStorage.getItem("jwtToken"));
if (tokenData) {
  axios.defaults.headers.common["Authorization"] = `Token ${tokenData.token}`;
  store.commit("setUser", tokenData);
}

import "./styles/colors.css";

Vue.config.productionTip = false;

new Vue({
  router,
  store,
  render: (h) => h(App),
}).$mount("#app");
