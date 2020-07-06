import axios from 'axios';

async function register (userData){
  const url = '/api/accounts/register/';
  const response = await axios.post(url, userData);
  return response.data;
}

async function login (userData){
  const url = '/api/accounts/login/';
  const response = await axios.post(url, userData);
  setAuthToken(response.data);
  return response.data;
}

async function logout() {
  const url = '/api/accounts/logout/';
  await axios.post(url);
}

function setAuthToken(tokenData) {
  localStorage.setItem('jwtToken', JSON.stringify(tokenData));
  const authHeader = `Token ${tokenData.token}`;
  axios.defaults.headers.common['Authorization'] = authHeader;
}

export default{
  register,
  login,
  logout,
};
