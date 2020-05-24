<template>
  <div>
    <router-link
      :to="{ name: 'recipe-create'}"
      tag="button"
      class="absolute bottom-0 right-0 pantry-bg-brown cursor-pointer text-white p-2 m-2 border border-gray-400 shadow rounded-full h-16 w-16"
    >
      <span class="flex items-start">
        <i class="material-icons md-24">restaurant</i>
        <i class="material-icons md-8">add</i>
      </span>
    </router-link>
    <div class="flex justify-center">
      <div
        v-for="recipe in recipes" :key="recipe.id"
        class="max-w-sm rounded bg-white overflow-hidden shadow-lg m-8"
      >
        <img class="w-full" :src="recipeImageUrl" alt="Sunset in the mountains">
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
import axios from 'axios';
export default {
  name: 'Recipes',
  data() {
    return {
      recipes: [],
      recipeImageUrl: 'http://www.howtodecorate.com/wp-content/uploads/2014/03/25_place_settings_spa.jpg',
    };
  },
  async mounted() {
    const response = await axios.get('/api/recipes');
    this.recipes = response.data;
  },
};
</script>
