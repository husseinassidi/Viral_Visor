import axios from 'axios';
import FormData from 'form-data';

async function Login(username, password) {
  const url = 'http://127.0.0.1:8080/login';
  const formData = new FormData();
  formData.append('username', username);
  formData.append('password', password);
  try {
    const response = await axios.post(url, formData, {
      headers: {
        ...formData.getHeaders(),  
      }
    });
    localStorage.setItem('access_token', response.data.access_token);
    localStorage.setItem('token_type', response.data.token_type);
    console.log('Login successful:', response.data);
  } catch (error) {
    if (error.response) {
      console.error('Login failed:', error.response.data?.detail || error.response.statusText);
    } else {
      console.error('Login failed: Network error or server is unreachable', error.message);
    }
  }
}


export default Login_service;