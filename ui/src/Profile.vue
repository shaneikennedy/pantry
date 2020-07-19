<template>
  <div class="container mx-auto pt-8">
    <div class="max-w-full mx-auto rounded overflow-hidden shadow-lg">
      <user-info :profile="profile" />
      <ul class="flex justify-center py-1">
        <li class="mr-3">
          <a
            class="inline-block border border-white rounded pantry-text-brown hover: py-1 px-3"
            :class="{'activeTab':currentTab === 'user-recipes'}"
            href="#"
            @click="currentTab = 'user-recipes'"
          >My Recipes</a>
        </li>
        <li class="mr-3">
          <a
            class="inline-block border border-white rounded pantry-text-brown hover: py-1 px-3"
            :class="{'activeTab':currentTab === 'user-likes'}"
            href="#"
            @click="currentTab = 'user-likes'"
          >Liked Recipes</a>
        </li>
      </ul>
    </div>
    <div class="flex" v-if="currentTab === 'user-recipes'">
      <div v-for="recipe in profile.recipes" :key="recipe.id" @click="goToDetailsPage(recipe.id)">
        <recipe-card :recipe="recipe" />
      </div>
    </div>
    <div class="flex" v-if="currentTab === 'user-likes'">
      <div v-for="recipe in profile.likes" :key="recipe.id" @click="goToDetailsPage(recipe.id)">
        <recipe-card :recipe="recipe" />
      </div>
    </div>
  </div>
</template>

<script>
import userApi from "./api/user";
import RecipeCard from "./components/RecipeCard";
import UserInfo from "./components/UserInfo";

export default {
  name: "Profile",
  components: { RecipeCard, UserInfo },
  data() {
    return {
      profile: {
        username: "",
        email: "",
        date_joined: "",
        recipes: [],
        likes: []
      },
      currentTab: "user-recipes"
    };
  },
  async mounted() {
    this.profile = await userApi.getUser();
  },
  methods: {
    goToDetailsPage(recipeId) {
      this.$router.push({
        name: "recipe-info",
        params: { recipe_id: recipeId }
      });
    }
  }
};
</script>
<style scoped>
.activeTab {
  background-color: var(--pantry-brown);
  color: white;
}
</style>