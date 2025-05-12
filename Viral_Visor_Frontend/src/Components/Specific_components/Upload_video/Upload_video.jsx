import React, { useState } from 'react';
import axios from 'axios';
import illust from "/assets/upload_illustration.svg"; // Example: Update the path based on your project
import "./Upload_video.css"
const audienceTypes = [
    "Developers", "Content Creators", "Influencers", "Gamers", "Entrepreneurs", 
    "Bloggers", "Marketers", "Students", "Photographers", "Designers", 
    "Fitness Enthusiasts", "Travelers", "Musicians", "Fashion Enthusiasts", 
    "Podcasters", "Vloggers", "Business Owners", "Foodies", "Tech Enthusiasts", 
    "Investors"
];

const UploadVideo = () => {
    const [inputValue, setInputValue] = useState('');
    const [goalList, setGoalList] = useState([]);
    const [keywordValue, setKeywordValue] = useState('');
    const [keywordList, setKeywordList] = useState([]);
    const [videoFile, setVideoFile] = useState(null);
    const [videoError, setVideoError] = useState('');
    
    const [uploadProgress, setUploadProgress] = useState(0); // For showing progress

    const handleGoalKeyPress = (e) => {
        if (e.key === 'Enter' && inputValue.trim() !== '') {
            const newGoal = inputValue.trim();
            setGoalList([...goalList, newGoal]);
            setInputValue(''); 
            e.preventDefault();
        }
    };

    const handleKeywordKeyPress = (e) => {
        if (e.key === 'Enter' && keywordValue.trim() !== '') {
            const newKeyword = keywordValue.trim();
            setKeywordList([...keywordList, newKeyword]);
            setKeywordValue(''); 
            e.preventDefault();
        }
    };

    const handleDrop = (e) => {
        e.preventDefault();
        const file = e.dataTransfer.files[0];
        if (file && file.type.startsWith('video/')) {
            const video = document.createElement('video');
            video.src = URL.createObjectURL(file);

            video.onloadedmetadata = () => {
                if (video.duration > 60) { // 60 seconds = 1 minute
                    setVideoError('Video is longer than 1 minute. Please upload a shorter video.');
                    setVideoFile(null);
                } else {
                    setVideoFile(file);
                    setVideoError('');
                }
            };
        } else {
            setVideoError('Please upload a valid video file.');
        }
    };

    const handleDragOver = (e) => {
        e.preventDefault();
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        
        if (!videoFile) {
            setVideoError('Please upload a video before submitting.');
            return;
        }

        const token = sessionStorage.getItem("access_token")

        const formData = new FormData();
        formData.append('title', e.target.title.value);
        formData.append('audience', e.target.audience.value);
        formData.append('goals', goalList.join(','));
        formData.append('keywords', keywordList.join(','));
        formData.append('file', videoFile);
        formData.append('access_token', token); 
        formData.append('token_type', 'bearer');

        try {
            const response = await axios.post('http://127.0.0.1:8080/upload/', formData, {
                headers: {
                    'Authorization': `Bearer your_actual_token`, // Replace with your token
                    'Content-Type': 'multipart/form-data',
                },
                onUploadProgress: (progressEvent) => {
                    const percentCompleted = Math.round((progressEvent.loaded * 100) / progressEvent.total);
                    setUploadProgress(percentCompleted); // Update the progress bar
                }
            });

            console.log('Response:', response.data);
            // Optionally reset the form
            setInputValue('');
            setGoalList([]);
            setKeywordValue('');
            setKeywordList([]);
            setVideoFile(null);
            setUploadProgress(0);

        } catch (error) {
            console.error('Error uploading video:', error);
            setVideoError('Failed to upload video. Please try again.');
        }
    };

    return (
        <section>
            <form className="Upload_form" onSubmit={handleSubmit}>
                <h1>Upload Your 1 Minute Reel</h1>
                <input className="upload_input" type="text" name="title" placeholder="Video Title" />

                <select name="audience">
                    <option value="">Select Audience Type</option>
                    {audienceTypes.map((audience, index) => (
                        <option key={index} value={audience.toLowerCase().replace(/\s+/g, '_')}>
                            {audience}
                        </option>
                    ))}
                </select>

                {/* Input for Goals */}
                <div className="upload_list">
                    <input className="upload_input"
                        type="text"
                        value={inputValue}
                        onChange={(e) => setInputValue(e.target.value)}
                        onKeyDown={handleGoalKeyPress}
                        placeholder="Add a goal and press Enter"
                    />
                    <ul className='word_list'>
                        {goalList.map((goal, index) => (
                            <li key={index}>{goal}</li>
                        ))}
                    </ul>
                </div>

                {/* Input for Keywords */}
                <div className="upload_list">
                    <input className="upload_input"
                        type="text"
                        value={keywordValue}
                        onChange={(e) => setKeywordValue(e.target.value)}
                        onKeyDown={handleKeywordKeyPress}
                        placeholder="Add a keyword and press Enter"
                    />
                    <ul lassName='word_list'>
                        {keywordList.map((keyword, index) => (
                            <li key={index}>{keyword}</li>
                        ))}
                    </ul>
                </div>

                {/* Drag-and-Drop Area */}
                <div className="drag_n_drop_video"
                    onDrop={handleDrop}
                    onDragOver={handleDragOver}
                    style={{
                        border: '2px dashed #ff1f00',
                        padding: '20px',
                        textAlign: 'center',
                        marginTop: '20px',
                        cursor: 'pointer'
                    }}
                >
                    {videoFile ? (
                        <p>Video Uploaded: {videoFile.name}</p>
                    ) : (
                        <p>Drag and drop a video here (Max: 1 minute)</p>
                    )}
                </div>

                {videoError && <p style={{ color: 'red' }}>{videoError}</p>}

                {/* Progress bar */}
                {uploadProgress > 0 && (
                    <div className="progress-bar">
                        <div className="progress" style={{ width: `${uploadProgress}%` }}>
                            {uploadProgress}% uploaded
                        </div>
                    </div>
                )}

                <button className="save_video" type="submit" style={{ marginTop: '20px' }}>Generate script</button>
            </form>
        </section>
    );
};

export default UploadVideo;
