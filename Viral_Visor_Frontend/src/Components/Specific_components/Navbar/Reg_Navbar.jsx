import React from 'react';
import logo from '../../../assets/General assets/logo.svg'; 
import "./Reg_Navbar.css";
import { useNavigate } from 'react-router-dom';

const Reg_Navbar = () => {
    const navigate = useNavigate();  // Hook for navigation

    const handleLogoClick = () => {
        navigate('/');  // Navigate to the home page
    };

    const logout = () => {
        // Clear session storage
        sessionStorage.removeItem("access_token");
        sessionStorage.removeItem("token_type");
        sessionStorage.removeItem("user_id");

        // Redirect to the login page or home page
        navigate('/'); // Assuming you want to redirect to the login page after logout
    };

    return (
        <div className='Reg-Navbar'>
            <img src={logo} alt="Logo" onClick={handleLogoClick} />
            <button className='logout_btn' onClick={logout}>Log out</button>
        </div>
    );
};

export default Reg_Navbar;
