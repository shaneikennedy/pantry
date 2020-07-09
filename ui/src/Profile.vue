<template>
  <div class="container mx-auto pt-8">
    <user-info :profile="profile" />
    <div v-for="recipe in profile.recipes" :key="recipe.id" @click="goToDetailsPage(recipe.id)">
      <recipe-card :recipe="recipe" />
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
      profile: { username: "", email: "", date_joined: "", recipes: [] }
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
