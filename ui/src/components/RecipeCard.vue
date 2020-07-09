<template>
  <div
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
</template>

<script>
import { defaultRecipeImageUrl } from "../utils";

export default {
  name: "RecipeCard",
  props: {
    recipe: {
      type: Object,
      required: true,
    },
  },
  data() {
    return {
      recipeImageUrl: defaultRecipeImageUrl
    };
  },
};
</script>
