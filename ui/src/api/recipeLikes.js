import axios from "axios";

async function likeRecipe(payload) {
    const url = '/api/accounts/user/likes';
    const response = await axios.post(url, payload);
    return response.data;
}

function unlikeRecipe(likeId) {
    const url = `/api/accounts/user/likes/${likeId}`;
    axios.delete(url);
}

export default {
  likeRecipe,
  unlikeRecipe,
};
