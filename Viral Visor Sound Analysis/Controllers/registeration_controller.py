from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from passlib.context import CryptContext
from Models.user_model import User
from schemas.user_schema import UserCreate, UserResponse
from database import get_db  # Assuming you have a get_db function for dependency injection
from dotenv import load_dotenv
from services.utils import hash_pass



# Initialize FastAPI Router and Password hashing
router = APIRouter()
load_dotenv()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    """Hash the password using bcrypt."""
    return pwd_context.hash(password)

@router.post("/register/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")

    # Hash the password
    hashed_password = hash_pass(user.password)

    # Create a new user instance
    new_user = User(
        email=user.email,
        password=hashed_password,
        first_name=user.first_name,
        last_name=user.last_name,
        user_name=user.user_name,
        birthday=user.birthday,
        University=user.University,
        Country=user.Country
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

