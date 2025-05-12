from sqlalchemy.orm import Session
from Models.admin_model import Admin  # Assuming models.py holds the Admin model
from schemas.admin_schema import AdminCreate
from passlib.hash import bcrypt  # For password hashing


def get_admin_by_email(db:Session, email: str):
        """
        Fetch an admin by their email address.
        
        :param email: Admin's email
        :return: Admin object or None if not found
        """
        return db.query(Admin).filter(Admin.email == email).first()

def get_admin_by_id(db:Session, admin_id: int):
        """
        Fetch an admin by their ID.
        
        :param admin_id: Admin's ID
        :return: Admin object or None if not found
        """
        return db.query(Admin).filter(Admin.id == admin_id).first()

def get_admin_by_username(db: Session, username: str):
    return db.query(Admin).filter(Admin.user_name == username).first()
