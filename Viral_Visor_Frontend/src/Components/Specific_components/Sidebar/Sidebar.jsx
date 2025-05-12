import React, { useEffect, useState } from "react";
import "./Sidebar.css";
import axios from "axios";

const Sidebar = ({onGetting_script}) => {
  // Initialize state for audios
  const [audios, setAudios] = useState([]);
  const [error, setError] = useState(null); // Handle errors
  const user_id = sessionStorage.getItem("user_id");
  const token = sessionStorage.getItem("access_token");

  // // Handle fetching the script for a specific audio
  // const handle_getting_script = async (id) => {
  //   const data = new FormData(); // Using native FormData

  //   const config = {
  //     method: "get",
  //     maxBodyLength: Infinity,
  //     url: `http://127.0.0.1:8080/script/${id}`,
  //     headers: {
  //       Authorization: `Bearer ${token}`,
  //     },
  //   };

  //   try {
  //     const response = await axios.request(config);
  //     console.log("Script Data:", JSON.stringify(response.data));
  //   } catch (error) {
  //     console.error("Error fetching script:", error);
  //   }
  // };

  useEffect(() => {
    const fetchAudios = async () => {
      const config = {
        method: "get",
        maxBodyLength: Infinity,
        url: `http://127.0.0.1:8080/audio-track/${user_id}`,
        headers: {
          Authorization: `Bearer ${token}`,
        },
      };

      try {
        const response = await axios.request(config);
        setAudios(response.data); // Set audios in state
      } catch (error) {
        console.error("Error fetching audios:", error);
        setError("Failed to fetch audio tracks");
      }
    };

    fetchAudios();
  }, [user_id, token]); // Ensure useEffect depends on user_id and token

  return (
    <aside className="Sidebar_container">
      <h2>Sidebar</h2>

      {/* Display error if it exists */}
      {error && <p style={{ color: "red" }}>{error}</p>}

      {/* Display audio tracks */}
      {audios.length > 0 ? (
        audios.map((audio) => (
          <h1
            key={audio.id}
            id={audio.id}
            className="audio_card"
            onClick={() => onGetting_script(audio.id,token)} // Properly passing the callback
          >
            {audio.title}
          </h1>
        ))
      ) : (
        <p>No audio tracks available</p> // Fallback if no audios are fetched
      )}
    </aside>
  );
};

export default Sidebar;
