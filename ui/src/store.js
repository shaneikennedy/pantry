import Vue from 'vue';
import Vuex from 'vuex';

import authAPI from './api/auth';
import userAPI from './api/user';

Vue.use(Vuex);

const store = new Vuex.Store({
  state: {
    user: null,
    profile: null,
  },
  mutations: {
    setUser (state, user) {
      state.user = user;
    },
    setProfile(state, profile) {
      state.profile = profile;
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
    },
    async fetchUserProfile(context) {
      const profile = await userAPI.getUser();
      context.commit("setProfile", profile);
    },
  }
});

export default store;
