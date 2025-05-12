import React from "react";
import { useTypewriter, Cursor } from 'react-simple-typewriter';
import "./text_animation.css";

function Text_animation({ onRegisterButtonClick }) {
  const [text] = useTypewriter({
    words: ['Influencers...', 'Content Creators...', 'Vloggers...', 'Bloggers...', 'Podcastors...','Any One...'],
    loop: true, 
    delaySpeed: 2000,  
    typeSpeed: 100,  
    deleteSpeed: 50, 
  });

  return (
    <div className="text_animation_container">
      <h1 style={{margin: '0px 150px', color:"white", textAlign:"left", fontSize:'5rem'}}>
        Speak Your Vision, See It Come to Life.
      </h1>
      <h1 style={{ margin: '0px 150px', color:"#0FCABF", fontSize:'4rem', textAlign:"left" }}>
        An AI Powered Assistant For {'\n '}
        <br />
        <span style={{ fontWeight: 'bold', color: 'red' }}>
          {text}
        </span>
        <Cursor cursorStyle='|' cursorColor='red' />
      </h1>
      <button className="register_btn" onClick={onRegisterButtonClick}>
        Join the Creation Revolution
      </button>
    </div>
  );
}

export default Text_animation;
