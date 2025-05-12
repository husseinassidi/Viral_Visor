from sqlalchemy.orm import Session
from Models import articles_model
from database import get_db


def delete_article(db: Session, article_id: int):
    db_article = db.query(articles_model).filter(articles_model.id == article_id).first()
    
    if db_article is None:
        return None  # Or raise an exception
    
    db.delete(db_article)
    db.commit()
    return db_article