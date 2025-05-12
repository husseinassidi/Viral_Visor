import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom'; // Import useNavigate
import "./login.css";

// Adjust the Login function to remove navigate
async function Login(username, password) {
  const url = 'http://127.0.0.1:8080/login';
  const formData = new FormData();
  formData.append('username', username);
  formData.append('password', password);

  try {
    const response = await axios.post(url, formData);
    
    sessionStorage.setItem('access_token', response.data.access_token);
    sessionStorage.setItem('token_type', response.data.token_type);
    sessionStorage.setItem('user_id', response.data.user_id);

    console.log('Login successful:', response.data);

    return response.data;
  } catch (error) {
    if (error.response) {
      console.error('Login failed:', error.response.data?.detail || error.response.statusText);
    } else {
      console.error('Login failed: Network error or server is unreachable', error.message);
    }
    throw error; 
  }
}

function LoginForm({ onLoginButtonClick }) {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState(null);
  const navigate = useNavigate(); // Initialize useNavigate

  const handleLogin = async (e) => {
    e.preventDefault();
    try {
      const data = await Login(username, password);
      console.log('Login successful:', data);

      // Redirect to the Homepage route upon successful login
      navigate('/Home'); // Use navigate to redirect
    } catch (err) {
      setError('Login failed. Please try again.');
    }
  };

  return (
    <div className='login_form_container'>
      <button className='close_reg_form login_close_btn' onClick={onLoginButtonClick}>X</button>

      <form onSubmit={handleLogin} className='login_form'>
        <h1>Sign In</h1>
        <label>Username:</label>
        <input className='login_input'
          type="text"
          placeholder="Username"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          required
        />
        <label>Password:</label>
        <input className='login_input'
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
        />
        <button type="submit">Login</button>
      </form>
      {error && <p style={{ color: 'red' }}>{error}</p>}
    </div>
  );
}

export default LoginForm;
