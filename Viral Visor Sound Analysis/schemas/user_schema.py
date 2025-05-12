from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from datetime import date

class UserBase(BaseModel):
    email: Optional[str] = None
    password: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    user_name: Optional[str] = None
    birthday: Optional[datetime] = None
    University: Optional[str] = None
    Country: Optional[str] = None

class UserCreate(UserBase):
    email: str
    password: str
    first_name: str
    last_name: str
    user_name: str
    birthday: datetime
    Country: str

class UserUpdate(UserBase):
    pass

class User(UserBase):
    id: int

    class Config:
        orm_mode = True



class UserResponse(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str
    user_name: str
    birthday: Optional[date]
    University: Optional[str]
    Country: Optional[str]

    class Config:
        orm_mode = True  # Allows the Pydantic model to work with SQLAlchemy objects