import os
from moviepy.editor import VideoFileClip
from sqlalchemy.orm import Session
from Models.audiotracks import AudioFile
from database import SessionLocal
import logging
from dotenv import load_dotenv

load_dotenv()

Upload_Folder = os.getenv("STORAGE_DIRECTORY")



def extract_audio_from_video(video_path: str, filename: str) ->str:


#  The audio extracting kernel
    video = VideoFileClip(video_path)
    audio_filename= os.path.splitext(filename)[0]+".mp3"
    audio_path = os.path.join(Upload_Folder,audio_filename)
    logging.info(audio_path)


# does the upload folder exists?
    os.makedirs(Upload_Folder, exist_ok=True)

# write the audio file
    video.audio.write_audiofile(audio_path,codec='mp3')
    video.close()
    logging.info(audio_path)

    return audio_path

# saving the audiofile path into the database

def save_audio(file_path: str, filename: str, title: str, audience: str, goals: list, keywords: list,user_id = str) -> AudioFile:
    db: Session = SessionLocal()
    try:
        audio_file = AudioFile(
            filename=filename,
            file_path=file_path,
            title=title,
            audience=audience,
            goals=goals,
            keywords=keywords,
            user_id= int(user_id)
        )
        db.add(audio_file)
        db.commit()
        db.refresh(audio_file)
        return audio_file
    finally:
        db.close()


def get_audio_info(audio_id: int) -> AudioFile:
    """
    This function retrieves all columns of an audio file entry from the database
    based on the audio_id.
    
    Args:
        audio_id (int): The ID of the audio file.

    Returns:
        AudioFile: The full audio file object with all columns, or None if not found.
    """
    db: Session = SessionLocal()
    try:
        # Query the database for the audio file with the specified ID
        audio_file = db.query(AudioFile).filter(AudioFile.id == audio_id).first()

        return audio_file  # Return the full AudioFile object with all columns
    finally:
        db.close()

def get_audio_name(audio_id: int) -> str:
    db: Session = SessionLocal()
    try:
        audio_file = db.query(AudioFile).filter(AudioFile.id == audio_id).first()
        if audio_file:

            return audio_file.filename
    finally:
        db.close()
    return None

