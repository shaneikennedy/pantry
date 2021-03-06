import Vue from 'vue';
import Vuex from 'vuex';

import authAPI from './api/auth';
import userAPI from './api/user';
import recipeAPI from "./api/recipe";
import recipeLikesApi from "./api/recipeLikes";


Vue.use(Vuex);

const store = new Vuex.Store({
  state: {
    user: null,
    profile: null,
  },
  mutations: {
    setUser(state, user) {
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
      context.commit('setProfile', null);
    },
    async fetchUserProfile(context) {
      const profile = await userAPI.getUser();
      context.commit("setProfile", profile);
    },
    async createRecipe(context, payload) {
      await recipeAPI.addRecipe(payload);
      context.dispatch("fetchUserProfile");
    },
    async likeRecipe(context, payload) {
      await recipeLikesApi.likeRecipe(payload);
      context.dispatch("fetchUserProfile");
    },
    async unlikeRecipe(context, likeId) {
      await recipeLikesApi.unlikeRecipe(likeId);
      context.dispatch("fetchUserProfile");
    },
  }
});

export default store;
