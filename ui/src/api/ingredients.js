import axios from "axios";

async function getIngredients() {
  const response = await axios.get("/api/ingredients");
  return response.data;
}
export default {
  getIngredients
};
