from sqlalchemy import Column, Integer, String,ForeignKey
from sqlalchemy.dialects.postgresql import JSON  # Import JSON type
from database import Base

class AudioFile(Base):
    __tablename__ = 'audio_files'

    
    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, index=True)
    file_path = Column(String, nullable=False)
    title = Column(String, nullable=False)   # Title of the audio file
    audience = Column(String, nullable=False)  # Target audience
    goals = Column(JSON, nullable=True)  # List of goals (stored as JSON)
    keywords = Column(JSON, nullable=True)  # List of keywords (stored as JSON)
    user_id = Column(Integer, ForeignKey('users.id')) 



