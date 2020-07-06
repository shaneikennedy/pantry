import axios from "axios";

async function getUser() {
  const response = await axios.get("/api/accounts/user");
  return response.data;
}

export default {
  getUser
};
