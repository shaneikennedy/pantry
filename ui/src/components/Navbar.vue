<template>
  <nav
    class="flex items-center justify-between flex-wrap pantry-bg-red p-4 max-h-full"
  >
    <div class="flex items-center flex-shrink-0 text-white mr-6">
      <img src="./logo.svg" style="width:100px;height:50px;" @click="home" />
    </div>
    <div class="block lg:hidden">
      <button
        class="flex items-center px-3 py-2 border rounded border-teal-400 hover:text-white hover:border-white"
      >
        <svg
          class="fill-current h-3 w-3"
          viewBox="0 0 20 20"
          xmlns="http://www.w3.org/2000/svg"
        >
          <title>Menu</title>
          <path d="M0 3h20v2H0V3zm0 6h20v2H0V9zm0 6h20v2H0v-2z" />
        </svg>
      </button>
    </div>
    <div class="w-full block flex-grow lg:flex lg:items-center lg:w-auto">
      <div class="text-sm lg:flex-grow">
        <router-link
          :to="{ name: 'recipes' }"
          class="block mt-4 lg:inline-block text-white lg:mt-0 hover:text-white mr-4"
        >
          Recipes
        </router-link>
      </div>
    </div>
    <button v-show="user" class="text-white" @click="logout">
      Logout
    </button>
    <button
      v-show="!user && this.$route.name === 'home'"
      class="text-white"
      @click="login"
    >
      Login
    </button>
  </nav>
</template>

<script>
import { mapState } from "vuex";

export default {
  name: "Navbar",
  computed: {
    ...mapState(["user"])
  },

  methods: {
    login() {
      this.$router.push({ name: "login" });
    },
    home() {
      this.$router.push({ name: "home" });
    },
    logout() {
      try {
        this.$store.dispatch("logoutUser");
        this.$router.push({ name: "login" });
      } catch (err) {
        console.error(err);
      }
    }
  }
};
</script>
