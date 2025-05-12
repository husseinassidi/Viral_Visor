import React, { useEffect, useState } from "react";
import logo from '../../../assets/General assets/logo.svg'; 
import './Landing_navbar.css';
import { useNavigate } from 'react-router-dom'; // Import useNavigate

const Landing_navbar = ({ onLoginButtonClick }) => {
    const [showHomeButton, setShowHomeButton] = useState(false);
    const navigate = useNavigate(); // Initialize useNavigate

    useEffect(() => {
        const accessToken = sessionStorage.getItem("access_token");
        console.log("Access Token:", accessToken); // Debugging log
        setShowHomeButton(accessToken !== null);
    }, []); // Empty dependency array means this runs once when the component mounts

    console.log("Show Home Button:", showHomeButton); // Debugging log

    return (
        <nav>
            <div><img src={logo} alt="Logo" /></div>
            <ul className="nav_list">
                <li><a href="#">About Us</a></li>
                <li><a href="#">How it Works</a></li>
                <li><a href="#">FAQs</a></li>
            </ul>

            {showHomeButton
                ? <button onClick={() => navigate("/Home")}>Home</button>
                : <button onClick={onLoginButtonClick}>Login</button>
            }
        </nav>
    );
};

export default Landing_navbar;
