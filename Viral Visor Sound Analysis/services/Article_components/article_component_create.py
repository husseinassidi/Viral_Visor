from sqlalchemy.orm import Session
from Models.article_components import Article_component  # Assuming the model is in Models folder
from schemas import article_component_schema  # Assuming you have a Pydantic schema

# Function to create a component
def create_component(db: Session, component_data: article_component_schema.ArticleComponentCreate):
    db_component = Article_component(
        component_type=component_data.component_type,
        content=component_data.content,
        content_order=component_data.content_order,
        article_id=component_data.article_id
    )
    db.add(db_component)
    db.commit()
    db.refresh(db_component)
    return db_component

# Function to get all components by article_id
def get_all_components_for_article_id(db: Session, article_id: int):
    return db.query(Article_component).filter(
        Article_component.article_id == article_id
    ).all()
