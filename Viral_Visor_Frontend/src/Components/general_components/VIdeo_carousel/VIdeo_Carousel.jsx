import React, { useRef } from 'react';
import './VideoCarousel.css';  // Import your CSS for styling
import video1 from '../../../assets/General assets/video1.mp4';
import video2 from '../../../assets/General assets/video2.mp4';
import video3 from '../../../assets/General assets/video3.mp4';
import forward from '../../../assets/General assets/forward-solid.svg';
import backward from '../../../assets/General assets/backward-solid.svg';

const VideoCarousel = () => {
  const videoContainerRef = useRef(null);

  // Function to scroll the container to the right
  const scrollRight = () => {
    videoContainerRef.current.scrollBy({ left: 1010, behavior: 'smooth' });
  };

  // Function to scroll the container to the left
  const scrollLeft = () => {
    videoContainerRef.current.scrollBy({ left: -1010, behavior: 'smooth' });
  };

  return (
    <div className="carousel-container">
      <button className="scroll-button left" onClick={scrollLeft}>
        <img src={backward} alt="" />
      </button>
      <div className="video-container" ref={videoContainerRef}>
        <video src={video1} autoPlay loop muted />
        <video src={video2} autoPlay loop muted />
        <video src={video3} autoPlay loop muted />
      </div>
      <button className="scroll-button right" onClick={scrollRight}>
      <img src={forward} alt="" />

      </button>
    </div>
  );
};

export default VideoCarousel;
