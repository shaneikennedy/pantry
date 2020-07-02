<template>
  <div class="container mx-auto pt-8">
    <div class="max-w-full mx-auto rounded overflow-hidden shadow-lg">
      <div class="pantry-bg-yellow2 p-4">
        <div class="h-16 w-16 bg-gray-400 rounded-full mx-auto">
          <p class="text-center text-white text-3xl">{{ profile.username[0] }}</p>
        </div>
        <span class="block text-gray-700 text-center px-4 py-2 text-xl">
          {{ profile.username }}
          <br />
        </span>
        <span class="block text-gray-700 text-center px-4 py-2 text-sm">
          User Since:
          {{ translateDate(profile.date_joined) }}
          <br />
        </span>
        <span class="block text-gray-700 text-center px-4 py-2 text-sm">
          Email: {{ profile.email }}
          <br />
        </span>
      </div>
      <div class="flex pantry-bg-yellow2">
        <div class="flex-1 text-gray-700 text-center .pantry-bg-yellow2 px-4 py-2 m-2">
          <button
            class="pantry-bg-brown text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
            type="submit"
          >Saved Recipes</button>
        </div>
        <div class="flex-1 text-gray-700 text-center .pantry-bg-yellow2 px-4 py-2 m-2">
          <button
            class="pantry-bg-brown text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
            type="submit"
          >My Recipes</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import userApi from "./api/user";

export default {
  data() {
    return {
      profile: { username: "", email: "", date_joined: "" }
    };
  },
  async mounted() {
    this.profile = await userApi.getUser();
  },
  methods: {
    translateDate(date) {
      return new Date(date).toDateString();
    }
  }
};
</script>
