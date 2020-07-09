<template>
  <div>
    <router-link
      :to="{ name: 'recipe-create' }"
      tag="button"
      class="absolute bottom-0 right-0 pantry-bg-brown cursor-pointer text-white p-2 m-2 border border-gray-400 shadow rounded-full h-16 w-16"
    >
      <span class="flex items-start">
        <i class="material-icons md-24">restaurant</i>
        <i class="material-icons md-8">add</i>
      </span>
    </router-link>
    <div class="flex flex-wrap justify-center">
      <div
        v-for="recipe in recipes"
        :key="recipe.id"
        @click="goToDetailsPage(recipe.id)"
      >
        <recipe-card :recipe="recipe" />
      </div>
    </div>
  </div>
</template>

<script>
import recipeApi from "./api/recipe";
import RecipeCard from './components/RecipeCard';

export default {
  name: "Recipes",
  components: { RecipeCard },
  data() {
    return {
      recipes: [],
    };
  },
  async mounted() {
    this.recipes = await recipeApi.getRecipes();
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
