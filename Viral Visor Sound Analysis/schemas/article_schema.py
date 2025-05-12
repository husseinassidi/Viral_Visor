from pydantic import BaseModel
from typing import Optional

# Base schema
class ArticleBase(BaseModel):
    title: str

# Schema for creating an Article
class ArticleCreate(ArticleBase):
    pass

# Schema for reading an Article (with id)
class ArticleRead(ArticleBase):
    id: int

    class Config:
        orm_mode = True
