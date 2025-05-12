from fastapi import APIRouter, File, UploadFile, HTTPException, Form, Depends,status,Header
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from services.audio_service import extract_audio_from_video, save_audio, get_audio_info
from services.text_service import speech_to_text
from services.script_formatting_services import format_text_for_script, script_exist
import os
import logging
from dotenv import load_dotenv
from typing import List, Optional
from services.auth_service import verify_token_access, get_current_user
from database import get_db
import schemas.auth_schema
from Models.audiotracks import AudioFile
from jose import JWTError



router =APIRouter()

load_dotenv()
@router.post("/upload/")
async def upload_video(
    file: UploadFile = File(...),  # File for the video
    title: str = Form(...),  # Form for title
    audience: str = Form(...),  # Form for audience
    goals: Optional[str] = Form(None),  # Form for goals, comma-separated string
    keywords: Optional[str] = Form(None),  # Form for keywords, comma-separated string
    access_token: str = Form(...),  # Token for authentication
    token_type: str = Form(...),  # Token type (if needed)
):
    """
    Endpoint to upload a video file, extract audio, and save metadata to the database.
    """
    try:
        # Define credentials exception for unauthorized access
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"}
        )

        # Verify the access token and get the user ID
        token_data, user_id = verify_token_access(access_token, credentials_exception)

        logging.info(f"Received file: {file.filename} from user {user_id}")

        # Save the uploaded video file to a temporary location
        temp_video_path = f"temp_{file.filename}"
        with open(temp_video_path, "wb") as f:
            f.write(file.file.read())
        logging.info(f"Video saved to: {temp_video_path}")

        # Extract the audio from the video and save it to the STORAGE_DIRECTORY
        audio_path = extract_audio_from_video(temp_video_path, file.filename)
        audio_filename = os.path.basename(audio_path)

        # Process goals and keywords from string to list (comma-separated input)
        goals_list = goals.split(",") if goals else []
        keywords_list = keywords.split(",") if keywords else []

        # Save the audio file with all the metadata including the user ID
        saved_audio = save_audio(
            file_path=audio_path, 
            filename=audio_filename, 
            title=title, 
            audience=audience, 
            goals=goals_list, 
            keywords=keywords_list, 
            user_id=user_id  # Add user ID here
        )

        return {"filename": saved_audio.filename, "id": saved_audio.id, "file_path": saved_audio.file_path}

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        # Clean up the temporary file
        if os.path.exists(temp_video_path):
            os.remove(temp_video_path)
# Use OAuth2PasswordBearer to retrieve the token from the Authorization header
oauth2_schema = OAuth2PasswordBearer(tokenUrl="token")

@router.get("/script/{audio_id}")
def get_audio_by_id(
    audio_id: int,
    token: str = Depends(oauth2_schema),  # Token extracted from the header
    db: Session = Depends(get_db)
):
    # Verify the token and get the current user
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    current_user = get_current_user(token=token, db=db)
    if not current_user:
        raise credentials_exception

    # Check if script already exists for this audio
    script, check = script_exist(audio_id=audio_id)
    if check:
        return {"script": script}

    # Fetch the audio file info (path and metadata) from the database or service layer
    audio_info = get_audio_info(audio_id)
    if not audio_info:
        raise HTTPException(status_code=404, detail="Audio file not found")

    # Convert the speech in the audio file to text
    try:
        text = speech_to_text(audio_info.file_path)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing audio: {str(e)}")

    # Format the text into a script based on audio metadata
    script = format_text_for_script(
        audio_id=audio_id,
        text=text,
        audience=audio_info.audience,
        title=audio_info.title,
        keywords=audio_info.keywords,
        goals=audio_info.goals
    )

    # (Optional) Save the newly generated script in the database

    # Re-check if the script exists after generation
    script, check = script_exist(audio_id=audio_id)
    if check:
        return {"script": script}

    # Return a success message with more detail if the script was created successfully
    return {"message": "Script created successfully", "audio_id": audio_id}


@router.get("/audio-track/{user_id}", response_model=List[dict])
async def get_user_audio_tracks(
    user_id: int,
    authorization: str = Header(...),  # Token from the Authorization header
    db: Session = Depends(get_db)
):
    """
    Fetch all audio tracks for a specific user by user ID.
    """
    try:
        # Extract the token from the Authorization header
        token = authorization.split(" ")[1]  # Assumes format "Bearer <token>"

        # Define the credentials exception
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"}
        )

        # Verify the token and get user_id from it
        token_data, token_user_id = verify_token_access(token, credentials_exception)
        token_user_id = int(token_user_id)
        # Check if the user_id from the token matches the user_id in the request
        if token_user_id != user_id:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Not authorized to access this user's audio tracks"
            )

        # Query the database for all audio files with the given user_id
        audio_tracks = db.query(AudioFile).filter(AudioFile.user_id == user_id).all()

        if not audio_tracks:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"No audio tracks found for user with ID {user_id}"
            )

        # Convert each SQLAlchemy model instance to a dictionary
        audio_tracks_dict = [track.__dict__ for track in audio_tracks]

        # Remove SQLAlchemy internal state key (_sa_instance_state)
        for track in audio_tracks_dict:
            track.pop('_sa_instance_state', None)
        logging.info(f"Request user_id: {user_id}")
        logging.info(f"Token user_id: {token_user_id}")

        return audio_tracks_dict

    except JWTError as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))