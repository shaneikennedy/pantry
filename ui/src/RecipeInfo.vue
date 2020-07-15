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
    <div class="flex justify-center">
      <div class="max-w-lg rounded bg-white overflow-hidden shadow-lg m-8">
        <img class="w-full" :src="recipeImageUrl" alt="Sunset in the mountains" />
        <div class="w-auto inline-block px-6 py-6">
          <div class="mb-2">
            <p class="font-bold text-xl">{{ recipe.name }}</p>
            <em class="text-md">By {{ recipe.author_username }}</em>
          </div>
          <p class="text-xl">Ingredients</p>
          <ul class="m-2">
            <div
              v-for="ingredient in recipe.ingredients"
              :key="ingredient.id"
              class="flex text-gray-700 capitalize text-base"
            >
              <p class="flex flex-1">{{ ingredient.quantity }}{{ unitsMap[ingredient.units] }}</p>
              <p class="flex flex-auto px-2">{{ ingredient.name }}</p>
            </div>
          </ul>
          <p class="text-xl py-4">Instructions</p>
          <div v-html="recipe.instructions"></div>
        </div>
        <div class="h-16 w-16 mr-0 mx-auto">
          <i class="cursor-pointer material-icons md-24" @click="likeRecipe">favorite_border</i>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import recipeApi from "./api/recipe";
import recipeLikesApi from "./api/recipeLikes";
import { defaultRecipeImageUrl, ingredientsUnitMap } from "./utils";

export default {
  name: "Recipe_info",
  data() {
    return {
      recipe: [],
      recipeImageUrl: defaultRecipeImageUrl,
      unitsMap: ingredientsUnitMap
    };
  },
  async mounted() {
    const recipeId = this.$route.params.recipe_id;
    this.recipe = await recipeApi.getRecipeDetail(recipeId);
  },
  methods: {
    async likeRecipe() {
      const payload = {
        recipe: this.recipe.id
      };
      await recipeLikesApi.likeRecipe(payload);
    }
  }
};
</script>
