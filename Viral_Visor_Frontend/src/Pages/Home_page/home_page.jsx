import Reg_Navbar from "../../Components/Specific_components/Navbar/Reg_Navbar";
import "./home_page.css";
import Sidebar from "../../Components/Specific_components/Sidebar/Sidebar";
import Display_script from "../../Components/Specific_components/Display_script/Display_Script";
import Upload_video from "../../Components/Specific_components/Upload_video/Upload_video";
import illust from "/assets/upload_illustration.svg";  
import illust2 from "/assets/red_ball.svg";
import axios from "axios";
import { useState } from "react";
import LoadingAnimation from "../../Components/Animations/three_balls_loading";

const Homepage = () => {
  const [currenScript, setCurrentScript] = useState('');  // Store the script data
  const [isDisplayed, setIsDisplayed] = useState(false);  // Controls display of script or upload section
  const [isLoading, setIsLoading] = useState(false);      // Controls loading animation display

  const back = (e) => {
    e.preventDefault();
    setIsDisplayed(false);
  };

  const handle_getting_script = async (id, token) => {
    setIsLoading(true);  // Start the loading animation

    const config = {
      method: "get",
      maxBodyLength: Infinity,
      url: `http://127.0.0.1:8080/script/${id}`,
      headers: {
        Authorization: `Bearer ${token}`,
      },
    };

    try {
      const response = await axios.request(config);
      setCurrentScript(response.data);
      setIsDisplayed(true);  // Show the script
    } catch (error) {
      console.error("Error fetching script:", error);
    } finally {
      setIsLoading(false);  // Stop the loading animation
    }
  };

  return (
    <div className="Home_Page_container">
      <Reg_Navbar />
      
      <div className="home_main">
        <Sidebar onGetting_script={handle_getting_script} />
        
        <div className="upload_video_sec">
          {!  isDisplayed&&<img src={illust2} style={{ height: "100px" }} alt="" />}

          {/* Display Loading Animation if loading, else display script or upload video */}
          {isLoading ? (
            <LoadingAnimation />
          ) : isDisplayed ? (
            <Display_script script_lines_data={currenScript} />
          ) : (
            <Upload_video />
          )}

          {!isDisplayed &&<img src={illust2} style={{ height: "100px" }} alt="" />}

          {isDisplayed && <button onClick={back} className="back_home">Back to Home</button>}
        </div>
      </div>
    </div>
  );
};

export default Homepage;
