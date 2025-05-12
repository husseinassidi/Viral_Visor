import React, { useState } from "react"; 
import "./Landing_page.css";
import Landing_navbar from "../../Components/general_components/Landing_navbar/Landing_navbar";
import VideoCarousel from "../../Components/general_components/Video_carousel/Video_Carousel";
import RV_cards from "../../Components/general_components/Review_cards/RV_cards";
import Text_animation from "../../Components/general_components/Intro_Animation/text_Animation"; 
import Footer from "../../Components/general_components/Footer/Footer";
import RegisterForm from "../Register_page/Register";
import LoginForm from "../../Components/general_components/Login/Login";
const Landing_page = () => {
  const [showRegisterForm, setShowRegisterForm] = useState(false);

  const handleRegisterButtonClick = () => {
    setShowRegisterForm(!showRegisterForm);
  };
  const [showLoginForm, setShowLoginForm] = useState(false);

  const handleLoginButtonClick = () => {
    setShowLoginForm(!showLoginForm);
  };

  return (
    <main className="landing-page">
      <Landing_navbar  onLoginButtonClick={handleLoginButtonClick}  />
      <Text_animation onRegisterButtonClick={handleRegisterButtonClick} />
      <VideoCarousel />

      <h1 style={{color:"white", fontWeight:'500'}}>Reviews</h1>
      <RV_cards />
      {showRegisterForm && <RegisterForm  onRegisterButtonClick={handleRegisterButtonClick} />}
        {showLoginForm && <LoginForm  onLoginButtonClick={handleLoginButtonClick} />}

      <Footer/>
    </main>
  );
};

export default Landing_page;
