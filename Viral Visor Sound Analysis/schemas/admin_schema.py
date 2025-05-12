from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class AdminCreate(BaseModel):
    email: EmailStr
    password: str
    first_name: str
    last_name: str
    user_name: str
    role: Optional[str] = "admin"
    birthday: datetime