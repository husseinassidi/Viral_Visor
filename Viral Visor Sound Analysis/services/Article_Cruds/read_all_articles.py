from sqlalchemy.orm import Session
from Models import articles_model
from database import get_db


def get_articles(db: Session, skip: int = 0, limit: int = 10):
    return db.query(articles_model.Article).offset(skip).limit(limit).all()
