<template>
  <div>
    <router-link
      :to="{ name: 'recipe-create' }"
      tag="button"
      class="absolute bottom-0 right-0 pantry-bg-brown z-40 cursor-pointer text-white p-2 m-2 border border-gray-400 shadow rounded-full h-16 w-16"
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
        class="max-w-xs cursor-pointer rounded bg-white overflow-hidden shadow-lg hover:shadow-xl m-8 transform hover:-translate-y-1 hover:scale-103 transition duration-100 ease-in-out "
      >
        <img
          class="w-full"
          :src="recipeImageUrl"
          alt="Sunset in the mountains"
        />
        <div class="px-6 py-4">
          <div class="font-bold text-xl mb-2">{{ recipe.name }}</div>
          <p class="text-xl">Ingredients</p>
          <ul class="m-2">
            <p
              v-for="ingredient in recipe.ingredients"
              :key="ingredient.id"
              class="text-gray-700 capitalize text-base"
            >
              {{ ingredient.name }}
            </p>
          </ul>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import recipeApi from "./api/recipe";
import { defaultRecipeImageUrl } from "./utils";

export default {
  name: "Recipes",
  data() {
    return {
      recipes: [],
      recipeImageUrl: defaultRecipeImageUrl
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
