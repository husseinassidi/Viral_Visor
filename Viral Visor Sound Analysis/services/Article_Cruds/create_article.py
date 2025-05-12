from sqlalchemy.orm import Session
from Models.articles_model import Article
from schemas import article_schema



def create_article(db: Session, article: article_schema.ArticleCreate, user_id: int):
    db_article = Article(title=article.title, user_id=user_id)
    db.add(db_article)
    db.commit()
    db.refresh(db_article)
    return db_article