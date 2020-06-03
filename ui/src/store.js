import Vue from 'vue';
import Vuex from 'vuex';

import authAPI from './api/auth';

Vue.use(Vuex);

const store = new Vuex.Store({
  state: {
    user: null,
  },
  mutations: {
    setUser (state, user) {
      state.user = user;
    },
  },
  actions: {
    async registerUser(context, payload) {
      await authAPI.register(payload);
      const user = await authAPI.login(payload);
      context.commit('setUser', user);
    },
    async loginUser(context, payload) {
      const user = await authAPI.login(payload);
      context.commit('setUser', user);
    },
    async logoutUser(context) {
      await authAPI.logout();
      context.commit('setUser', null);
    }
  }
});

export default store;
