import React, { useEffect, useRef, useState } from 'react';
import "./display_script.css";

const Display_script = (props) => {
    const scrollRef = useRef(null);
    const [isScrolling, setIsScrolling] = useState(true);  // State to track if scrolling is active
    let counter = 1;

    useEffect(() => {
        const scrollContainer = scrollRef.current;

        // Function for smooth auto-scrolling
        const scroll = () => {
            if (scrollContainer && isScrolling) {
                scrollContainer.scrollBy({
                    top: 1, // Scroll by 1 pixel
                    behavior: 'smooth'
                });
            }
        };

        // Set an interval for the scrolling
        const intervalId = setInterval(scroll, 50); // Adjust the interval for smoothness

        // Function to toggle scrolling when spacebar is pressed
        const handleKeyPress = (e) => {
            if (e.code === "Enter") {  // Change "Tab" to "Enter"
                e.preventDefault();  // Prevent the default action (if needed)
                setIsScrolling(!isScrolling);
            }
        };
        

        // Add event listener for keydown
        window.addEventListener('keydown', handleKeyPress);

        // Clean up the event listener and interval when the component unmounts
        return () => {
            clearInterval(intervalId);
            window.removeEventListener('keydown', handleKeyPress);
        };
    }, [isScrolling]);

    return (
        <div className="display_text_section" ref={scrollRef}>
            {props.script_lines_data.script.map((line) => (
                <div className="script_card" id={line.id} key={line.id}>
                    <h3 className="line" style={{ textAlign: "left" }}>{counter++}- Line: {line.line}</h3>
                    <h4 className="tonality">Tonality: {line.tonality}</h4>
                    <h4 className="body_language">Body Language: {line.body_language}</h4>
                </div>
            ))}
        </div>
    );
}

export default Display_script;
