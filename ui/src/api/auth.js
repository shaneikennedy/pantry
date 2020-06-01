import axios from 'axios';

async function register (userData){
  const url = '/api/accounts/register/';
  const response = await axios.post(url, userData);
  return response.data;
}

async function login (userData){
  const url = '/api/accounts/login/';
  const response = await axios.post(url, userData);
  setAuthToken(response.data.token);
  return response.data;
}

function setAuthToken(token) {
  localStorage.setItem('jwtToken', token);
  const authHeader = 'Token ' + localStorage.getItem('jwtToken');
  axios.defaults.headers.common['Authorization'] = authHeader;
}

export default{
  register,
  login,
};
