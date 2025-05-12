import React, { useState } from 'react';
import axios from 'axios';
import "./register.css"
import register_service from '../../Services/regiseter.js';

const RegisterForm = ({ onRegisterButtonClick }) => {
    // Define the initial form state
    const [formData, setFormData] = useState({
        email: "",
        user_name: "",
        password: "",
        first_name: "",
        last_name: "",
        birthday: "",
        University: "",
        Country: ""
    });

    const [responseMessage, setResponseMessage] = useState("");

    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData({ ...formData, [name]: value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();


        const config = {
            headers: {
                'Content-Type': 'application/json',
                'Accept': '*/*',
            }
        };
        
        axios.post('http://127.0.0.1:8080/register/', formData, config)
            .then(response => {
                console.log('Response:', response.data);
            })
            .catch(error => {
            if (error.response && error.response.data) {
                setResponseMessage( error.response.data.detail);
            } else {
                setResponseMessage("Error submitting form.");
            }
            });

            setFormData({
                email: "",
                user_name: "",
                password: "",
                first_name: "",
                last_name: "",
                birthday: "",
                University: "",
                Country: ""
            })
        
        
    };

    return (
        <div className='Form_container'>

            <div className='Register_form_header'>
            <h2>Register Form</h2>
            <button className='close_reg_form' onClick={onRegisterButtonClick}>X</button>

            </div>

            <form onSubmit={handleSubmit}  className='Register_form'>

                <div className='registeration_input_container'>
                    <label>Email:</label>
                    <input
                        type="email"
                        name="email"
                        placeholder='example@email.com'
                        value={formData.email}
                        onChange={handleChange}
                        required
                    />
                </div>
                <div className='registeration_input_container'>
                    <label>Username:</label>
                    <input
                        type="text"
                        name="user_name"
                        placeholder='User name'
                        value={formData.user_name}
                        onChange={handleChange}
                        required
                    />
                </div>
                <div className='registeration_input_container'>
                    <label>Password:</label>
                    <input
                        type="password"
                        name="password"
                        placeholder='Password'
                        value={formData.password}
                        onChange={handleChange}
                        required
                    />
                </div >
                <div className='registeration_input_container'>
                    <label>First Name:</label>
                    <input
                        type="text"
                        name="first_name"
                        placeholder='First name'
                        value={formData.first_name}
                        onChange={handleChange}
                        required
                    />
                </div>
                <div className='registeration_input_container'>
                    <label>Last Name:</label>
                    <input
                        type="text"
                        name="last_name"
                        placeholder='Last  name'

                        value={formData.last_name}
                        onChange={handleChange}
                        required
                    />
                </div >
                <div className='registeration_input_container'>
                    <label>Birthday:</label>
                    <input
                        type="date"
                        name="birthday"
                        value={formData.birthday}
                        onChange={handleChange}
                        required
                    />
                </div>
                <div className='registeration_input_container'>
                    <label>University:</label>
                    <input
                        type="text"
                        name="University"
                        placeholder='University'
                        value={formData.University}
                        onChange={handleChange}
                        required
                    />
                </div >
                <div className='registeration_input_container'>
                    <label>Country:</label>
                    <input
                        type="text"
                        name="Country"
                        value={formData.Country}
                        onChange={handleChange}
                        required
                    />
                </div >
                <button type="submit" className='register_form_btn'>Register</button>

            </form>

            {responseMessage && <p>{responseMessage}</p>}
        </div>
    );
};

export default RegisterForm;
