import axios from "axios";

async function likeRecipe(payload) {
    const url = '/api/accounts/user/likes';
    const response = await axios.post(url, payload);
    return response.data;
}
export default {
    likeRecipe
};