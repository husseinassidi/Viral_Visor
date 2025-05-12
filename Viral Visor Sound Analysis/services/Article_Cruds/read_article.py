from sqlalchemy.orm import Session
from Models import articles_model
from schemas import article_schema
from database import get_db



def get_article(db: Session, article_id: int):
    return db.query(articles_model).filter(articles_model.id == article_id).first()
