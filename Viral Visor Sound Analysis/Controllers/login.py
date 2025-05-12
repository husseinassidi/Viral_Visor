from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm

import Models.user_model
import schemas.auth_schema
import services.utils as utils
from database import get_db
from services.auth_service import create_access_token

router = APIRouter(tags=['Authentication'])

@router.post('/login', response_model=schemas.auth_schema.Token)
def login(userdetails: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    # Fetch user by email from the database
    user = db.query(Models.user_model.User).filter(Models.user_model.User.email == userdetails.username).first()

    # If user doesn't exist, raise an exception
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="The user does not exist"
        )

    # Verify if the provided password matches the hashed password in the database
    if not utils.verify_password(userdetails.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="The password does not match"
        )

    access_token = create_access_token(data={"user_id": user.id})

    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user_id": user.id  
    }
