from sqlalchemy import Column, Integer, String,ForeignKey,LargeBinary
from sqlalchemy.dialects.postgresql import JSON  # Import JSON type
from database import Base

class Article_component(Base):
    __tablename__ = 'Article_components'

    
    id = Column(Integer, primary_key=True, index=True)
    component_type = Column(String,  nullable=False)
    content = Column(LargeBinary,nullable=False)
    contet_order = Column(Integer,nullable=False)
    user_id = Column(Integer, ForeignKey('users.id')) 


