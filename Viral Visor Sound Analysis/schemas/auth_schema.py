from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from datetime import date

class Token(BaseModel):
    access_token: str
    token_type: str
    user_id: int  
class DataToken(BaseModel):
    id: Optional[str] = None