from sqlalchemy import Column, Integer, String,ForeignKey
from database import Base

class Article(Base):
    __tablename__ = 'Articles'

    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    user_id = Column(Integer, ForeignKey('users.id')) 


