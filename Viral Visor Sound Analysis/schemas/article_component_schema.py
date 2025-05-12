from pydantic import BaseModel
from typing import Optional

# Schema for creating a new Article component
class ArticleComponentCreate(BaseModel):
    component_type: str
    content: bytes
    content_order: int  # Corrected typo from 'contet_order' to 'content_order'
    article_id: int  # Changed from user_id to article_id to match the model

    class Config:
        orm_mode = True  # Enables compatibility with SQLAlchemy models
# Schema for updating an existing Article component
class ArticleComponentUpdate(BaseModel):
    component_type: Optional[str] = None
    content: Optional[bytes] = None
    contet_order: Optional[int] = None

# Schema for reading the Article component (output model)
class ArticleComponentRead(BaseModel):
    id: int
    component_type: str
    content: bytes
    content_order: int  # Corrected typo
    article_id: int  # Ensure this field matches your SQLAlchemy model

    class Config:
        orm_mode = True