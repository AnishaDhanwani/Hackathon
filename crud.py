from sqlalchemy.orm import Session
from . import models

# Create a new item in the database
def create_item(db: Session, name: str, description: str):
    db_item = models.Item(name=name, description=description)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

# Get all items from the database
def get_items(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Item).offset(skip).limit(limit).all()
