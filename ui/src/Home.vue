<template>
  <div class="container mx-auto pt-8">
    <div class="max-w-md mx-auto rounded overflow-hidden shadow-lg">
      <div class="px-6 py-4">
        <div class="font-bold text-xl mb-2">Register</div>
        <p class="text-gray-700 text-base mb-6">
          To get started with Pantry, sign up here
        </p>
        <form @submit.prevent="register">
          <div class="mb-4">
            <label class="block text-gray-700 text-sm font-bold mb-2" for="username">
              Username
            </label>
            <input
              class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
              id="username"
              type="text"
              required
              v-model="username"
              placeholder="Username"
            >
          </div>
          <div class="mb-4">
            <label class="block text-gray-700 text-sm font-bold mb-2" for="email">
              Email
            </label>
            <input
              class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
              id="Email"
              type="email"
              required
              v-model="email"
              placeholder="Email"
            >
          </div>
          <div class="mb-6">
            <label class="block text-gray-700 text-sm font-bold mb-2" for="password">
              Password
            </label>
            <input
              class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline"
              id="password"
              type="password"
              v-model="password"
              required
              placeholder="******************"
            >
          </div>
          <div class="flex items-center justify-between">
            <button class="pantry-bg-brown text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline" type="submit">
              Sign Up
            </button>
            <button><router-link to='/login'>Already a user? Login</router-link></button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import authAPI from './api/auth';

export default {
  name:'Home',
  data() {
    return {
      username: '',
      email: '',
      password: '',
    };
  },
  methods: {
    async register() {
      const payload = {
        username: this.username,
        email: this.email,
        password: this.password,
      };
      await authAPI.register(payload);
      await authAPI.login(payload);
      this.$router.push({ name: 'recipes' });
    },
  },
};
</script>
