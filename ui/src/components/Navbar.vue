<template>
  <nav
    class="flex items-center justify-between items-center flex-wrap pantry-bg-red p-4 max-h-full"
  >
    <img :src="logoUrl" class="w-20 h-10 mr-6 cursor-pointer" @click="home" />
    <div class="block lg:hidden">
      <button
        class="flex items-center px-3 py-2 border rounded border-teal-400 hover:text-white hover:border-white"
      >
        <svg class="fill-current h-3 w-3" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
          <title>Menu</title>
          <path d="M0 3h20v2H0V3zm0 6h20v2H0V9zm0 6h20v2H0v-2z" />
        </svg>
      </button>
    </div>
    <div class="w-full block flex-grow lg:flex lg:items-center lg:w-auto">
      <div class="lg:flex-grow">
        <router-link
          :to="{ name: 'recipes' }"
          class="block mt-4 lg:inline-block text-white lg:mt-0 hover:text-white mr-4"
          tag="button"
        >Recipes</router-link>
      </div>
    </div>
    <router-link
      v-if="profile"
      :to="{ name: 'profile' }"
      class="block mt-4 lg:inline-block text-white lg:mt-0 hover:text-white mr-4"
      tag="button"
    >{{ profile.username }}</router-link>
    <button v-show="user" class="text-white" @click="logout">Logout</button>
    <router-link v-show="isLoggedOut" class="text-white" tag="button" :to="{ name: 'login' }">Login</router-link>
  </nav>
</template>

<script>
import { mapState } from "vuex";
import LogoUrl from "../assets/logo.svg";

export default {
  name: "Navbar",
  computed: {
    ...mapState(["user", "profile"]),
    isLoggedOut() {
      return !this.user && this.$route.name === "home";
    }
  },
  data() {
    return {
      logoUrl: LogoUrl
    };
  },

  methods: {
    home() {
      this.$router.push({ name: "home" });
    },
    logout() {
      try {
        this.$store.dispatch("logoutUser");
        this.$router.push({ name: "home" });
      } catch (err) {
        console.error(err);
      }
    }
  }
};
</script>
