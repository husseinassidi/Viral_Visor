from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from services.Admin_services.Create_admin import create_admin  # Import function directly
from services.Admin_services.login_admin import get_admin_by_email, get_admin_by_id
from schemas.admin_schema import AdminCreate
from database import get_db  # Dependency to get the DB session

router = APIRouter()

@router.post("/admins/", status_code=status.HTTP_201_CREATED)
def create_new_admin(admin: AdminCreate, db: Session = Depends(get_db)):
    """
    Create a new admin user.
    
    :param admin: AdminCreate - Pydantic schema with admin details
    :param db: SQLAlchemy session (automatically injected via Depends)
    :return: The newly created admin object
    """
    # Check if the email or username already exists
    existing_admin = get_admin_by_email(db, admin.email)  # Pass db session to the function
    if existing_admin:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Admin with this email already exists"
        )

    existing_username = get_admin_by_id(db, admin.id)  # Pass db session to the function
    if existing_username:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Admin with this username already exists"
        )
    
    # Create the admin using the service function
    new_admin = create_admin(db, admin)  # Pass db session and admin data to the service function
    return new_admin
