from sqlalchemy.orm import Session
from Models import admin_model  # Assuming models.py holds the Admin model
from schemas.admin_schema import AdminCreate  # Define pydantic schemas for input validation
from passlib.hash import bcrypt  # For password hashing




def create_admin(db: Session, admin_data: AdminCreate):
    """
    Create a new admin in the database.
    
    :param db: SQLAlchemy Session
    :param admin_data: AdminCreate schema with admin details
    :return: The newly created admin object
    """
    hashed_password = bcrypt.hash(admin_data.password)  # Hash password
    new_admin = admin_model.Admin(
        email=admin_data.email,
        password=hashed_password,
        first_name=admin_data.first_name,
        last_name=admin_data.last_name,
        user_name=admin_data.user_name,
        role=admin_data.role,
        birthday=admin_data.birthday
    )
    db.add(new_admin)
    db.commit()
    db.refresh(new_admin)  # Refresh to get the new admin from the DB
    return new_admin