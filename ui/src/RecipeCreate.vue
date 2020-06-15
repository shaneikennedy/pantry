<template>
  <div class="flex flex-col m-4">
    <p class="text-3xl mb-8 mx-auto">Create a recipe</p>
    <form class="w-full max-w-lg mx-auto max-w-2xl" @submit.prevent="">
      <div class="-mx-3 mb-6">
        <div class="w-full px-3 mb-6 md:mb-0">
          <label
            class="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2"
            for="name"
            >Recipe name</label
          >
          <input
            class="appearance-none block w-full bg-gray-200 text-gray-700 border rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white"
            id="name"
            type="text"
            required
            v-model="name"
            placeholder="What is this recipe called?"
          />
        </div>
      </div>
      <div>
        <p class="text-lg">Ingredients</p>
        <div class="flex items-end justify-between py-4">
          <div>
            <label
              class="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2"
              for="quantity"
            >
              QUANTITY
            </label>
            <input
              class="appearance-none block w-full bg-gray-200 text-gray-700 border rounded py-1 leading-tight focus:outline-none focus:bg-white"
              id="quantity"
              type="number"
              v-model="newRecipeIngredient.quantity"
            />
          </div>
          <div>
            <label
              class="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2"
              for="Unit"
            >
              Units
            </label>
            <v-select
              id="Unit"
              class="w-32"
              :options="selectUnits"
              label="units"
              v-model="newRecipeIngredient.units"
            />
          </div>
          <div>
            <label
              class="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2"
              for="recipeIngredients"
            >
              Ingredient
            </label>
            <v-select
              id="recipeIngredients"
              :options="ingredients"
              class="w-64"
              label="name"
              v-model="newRecipeIngredient.ingredient"
            />
          </div>
          <div>
            <button
              class="pantry-bg-brown text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
              @click="addIngredient"
            >
              Add
            </button>
          </div>
        </div>
      </div>
      <div>
        <ul class="m-2">
          <div
            v-for="ingredient in recipeIngredients"
            :key="ingredient.ingredient.id"
            class="flex text-gray-700 capitalize text-base"
          >
            <p class="flex flex-1">
              {{ ingredient.quantity }}{{ unitsMap[ingredient.units] }}
            </p>
            <p class="flex flex-auto">{{ ingredient.ingredient.name }}</p>
            <i
              class="material-icons md-4 cursor-pointer"
              @click="removeRecipeIngredient(ingredient.ingredient.id)"
            >
              delete
            </i>
          </div>
        </ul>
      </div>

      <div class="-mx-3 mb-6">
        <div class="w-full px-3">
          <label
            class="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2"
            for="editor"
            >Instructions</label
          >
          <quill-editor
            id="editor"
            :options="editorOption"
            type="text"
            name="intructions"
            v-model="instructions"
          />
        </div>
      </div>
      <div>
        <button
          class="pantry-bg-brown text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
          @click="addRecipe"
        >
          Save
        </button>
      </div>
    </form>
  </div>
</template>

<script>
import "quill/dist/quill.core.css";
import "quill/dist/quill.bubble.css";
import "vue-select/dist/vue-select.css";

import vSelect from "vue-select";
import { quillEditor } from "vue-quill-editor";
import recipeAPI from "./api/recipe";
import { ingredientsUnitMap } from "./utils";
import ingredientAPI from "./api/ingredients";

const emptyNewIngredient = {
  quantity: null,
  units: null,
  ingredient: null
};

export default {
  name: "RecipeCreate",
  components: {
    quillEditor,
    vSelect
  },
  data() {
    return {
      editorOption: {
        theme: "bubble",
        placeholder: "How do you make this?",
        modules: {
          toolbar: [
            ["bold", "italic", "underline", "strike"],
            [{ list: "ordered" }, { list: "bullet" }],
            [{ header: [1, 2, 3, 4, 5, 6, false] }],
            [{ align: [] }],
            ["clean"]
          ]
        }
      },
      unitsMap: ingredientsUnitMap,
      ingredients: [],
      newRecipeIngredient: {
        quantity: null,
        units: null,
        ingredient: null
      },
      name: null,
      instructions: null,
      recipeIngredients: [],
      selectUnits: ["MG", "ML", "G", "KG", "L"]
    };
  },
  async mounted() {
    this.ingredients = await ingredientAPI.getIngredients();
  },
  methods: {
    addIngredient() {
      this.recipeIngredients.push({ ...this.newRecipeIngredient });
      this.newRecipeIngredient = { ...emptyNewIngredient };
    },
    removeRecipeIngredient(ingredientId) {
      this.recipeIngredients = this.recipeIngredients.filter(
        ing => ing.ingredient.id !== ingredientId
      );
    },
    async addRecipe() {
      try {
        const payload = {
          name: this.name,
          instructions: this.instructions,
          ingredients: this.recipeIngredients.map(val => ({
            quantity: val.quantity,
            units: val.units,
            ingredient: val.ingredient.id
          }))
        };
        await recipeAPI.addRecipe(payload);
        this.$router.push({ name: "recipes" });
      } catch (err) {
        console.log(err);
      }
    }
  }
};
</script>
