<template>
  <div id="app">
    Hello pantry
    <ul>
      <li v-for="ingredient in ingredients" :key="ingredient.id">
        {{ ingredient.name }}
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'App',
  data() {
    return {
      ingredients: [],
    };
  },
  async mounted() {
    const response = await axios.get('/api/ingredients');
    this.ingredients = response.data;
  },
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
