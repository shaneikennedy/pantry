import axios from "axios";

async function getRecipes() {
  const response = await axios.get("/api/recipes");
  return response.data;
}

async function getRecipeDetail(recipeId) {
  const response = await axios.get(`/api/recipes/${recipeId}`);
  return response.data;
}
function addRecipe(payload) {
  return axios.post(`/api/recipes`, payload);
}

export default {
  getRecipes,
  getRecipeDetail,
  addRecipe
};
