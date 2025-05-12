from sqlalchemy import Column, Integer, String, TIMESTAMP
from sqlalchemy.orm import declarative_base

from database import Base


class Admin(Base):
    __tablename__ = "Admin"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    user_name = Column(String, nullable=False, unique=True)
    role = Column(String, nullable =False, default="admin")
    birthday = Column(TIMESTAMP(timezone=True), nullable=False)

