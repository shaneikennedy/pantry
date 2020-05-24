<template>
  <div class="flex flex-col m-8">
    <p class="text-3xl mb-8 mx-auto">Create a recipe</p>
    <form class="w-full max-w-lg mx-auto">
      <div class="-mx-3 mb-6">
        <div class="w-full px-3 mb-6 md:mb-0">
          <label
            class="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2"
            for="grid-first-name"
          >
            Recipe name
          </label>
          <input
            class="appearance-none block w-full bg-gray-200 text-gray-700 border rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white"
            id="grid-first-name"
            type="text"
            placeholder="What is this recipe called?"
          >
        </div>
      </div>
      <div class="-mx-3 mb-6">
        <div class="w-full px-3">
          <label class="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" for="recipeIngredients">
            Ingredients
          </label>
          <v-select
            id="recipeIngredients"
            class="mb-2"
            :options="ingredients"
            @input="addIngredient"
            label="name"
          />
          <ul class="list-disc list-inside">
            <p
              class="my-4"
              v-if="!recipeIngredients.length"
            >
              Add some ingredients!
            </p>
            <li
              v-else
              v-for="recipeIngredient in recipeIngredients"
              :key="recipeIngredient.id"
              class="ml-4"
            >
              {{ recipeIngredient.name }}
            </li>
          </ul>
        </div>
      </div>
      <div class="-mx-3 mb-6">
        <div class="w-full px-3">
          <label class="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" for="editor">
            Instructions
          </label>
          <quill-editor
            id="editor"
            :options="editorOption"
          />
        </div>
      </div>
    </form>
  </div>
</template>

<script>
import 'quill/dist/quill.core.css';
import 'quill/dist/quill.bubble.css';
import 'vue-select/dist/vue-select.css';

import vSelect from 'vue-select'
import { quillEditor } from 'vue-quill-editor';
import axios from 'axios';

export default {
  name: 'RecipeCreate',
  components: {
    quillEditor,
    vSelect,
  },
  data() {
    return {
      editorOption: {
        theme: 'bubble',
        placeholder: 'How do you make this?',
        modules: {
          toolbar: [
            ['bold', 'italic', 'underline', 'strike'],
            [{ 'list': 'ordered'}, { 'list': 'bullet' }],
            [{ 'header': [1, 2, 3, 4, 5, 6, false] }],
            [{ 'align': [] }],
            ['clean'],
          ],
        },
      },
      ingredients: [],
      recipeIngredients: [],
    };
  },
  async mounted() {
    const response = await axios.get('/api/ingredients');
    this.ingredients = response.data;
  },
  methods: {
    addIngredient(ingredient) {
      this.recipeIngredients.push(ingredient);
    },
  },
};
</script>
