from fastapi import APIRouter, HTTPException, Header, Depends, status
from sqlalchemy.orm import Session
from schemas import article_schema
from dotenv import load_dotenv
from typing import Optional
from database import get_db
from services.auth_service import verify_token_access  # Import the function
from services.Article_Cruds.create_article import  create_article


router = APIRouter()

load_dotenv()

@router.post("/articles/", response_model=article_schema.ArticleRead)
def create_new_article(
    article: article_schema.ArticleCreate,  # Pydantic model to parse JSON body
    authorization: Optional[str] = Header(None),  # Optional Authorization header
    db: Session = Depends(get_db)
):
    # Check if Authorization header is missing
    if authorization is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Authorization header is missing",
            headers={"WWW-Authenticate": "Bearer"}
        )
    
    # Extract token from Authorization header
    try:
        scheme, token = authorization.split(" ")  # Assumes format "Bearer <token>"
        if scheme.lower() != "bearer":
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token scheme, expected 'Bearer'",
                headers={"WWW-Authenticate": "Bearer"}
            )
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid Authorization header format",
            headers={"WWW-Authenticate": "Bearer"}
        )
    
    # Verify the token and extract user ID
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"}
    )
    token_data, token_user_id = verify_token_access(token, credentials_exception)
    
    # Create article
    return create_article(db=db, article=article, user_id=token_user_id)