from sqlalchemy import Column, Integer, String, ForeignKey,TIMESTAMP, text
from sqlalchemy.dialects.postgresql import JSON  # Import JSON type
from database import Base



class Scripts(Base):
    __tablename__ = 'Scripts'

    id = Column(Integer, primary_key=True, index=True)
    line = Column(String, index=True)
    tonality = Column(String, index=True)
    body_language = Column(String, index=True)
    audio_track_id = Column(Integer, ForeignKey('audio_files.id')) 
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))


