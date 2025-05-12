from datetime import timedelta, datetime, timezone  # Add timezone for UTC aware objects
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from jose.exceptions import JWTError
from sqlalchemy.orm import Session
import schemas
from database import get_db
from dotenv import load_dotenv
import os
import Models.user_model
import schemas.auth_schema 

load_dotenv()

oauth2_schema = OAuth2PasswordBearer(tokenUrl='/login')
Secret_key = os.getenv("SECRET_KEY")
Expire_time = int(os.getenv("EXPIRE_TIME"))  # Make sure this is an integer, not the secret key
ALGORITHM = os.getenv("ALGORITHM")


def create_access_token(data: dict):
    to_encode = data.copy()

    expire = datetime.now(timezone.utc) + timedelta(minutes=Expire_time)

    # Update the token with the expiration time
    to_encode.update({"exp": expire})  # 'exp' is the JWT standard for expiry time

    # Encode the JWT token with the secret key and algorithm
    encoded_jwt = jwt.encode(to_encode, Secret_key, algorithm=ALGORITHM)

    return encoded_jwt


def verify_token_access(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, Secret_key, algorithms=ALGORITHM)
        id: str = payload.get("user_id")

        if id is None:
            raise credentials_exception

        # Convert id to string if it is not already
        if not isinstance(id, str):
            id = str(id)

        token_data = schemas.auth_schema.DataToken(id=id)
    except JWTError as e:
        print(e)
        raise credentials_exception

    # Return both token_data and id
    return token_data, id


def get_current_user(token: str = Depends(oauth2_schema), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not Validate Credentials",
        headers={"WWW-Authenticate": "Bearer"}
    )
    
    # Assuming verify_token_access returns a tuple: (token_data, token_user_id)
    token_data, token_user_id = verify_token_access(token, credentials_exception)
    
    # Query the user by the user ID from the token
    user = db.query(Models.user_model.User).filter(Models.user_model.User.id == token_user_id).first()
    
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    return user, token_user_id
