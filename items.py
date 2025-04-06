from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, models, database

router = APIRouter()

# Dependency to get the DB session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create a new item
@router.post("/item", response_model=models.Item)
async def place_item(name: str, description: str, db: Session = Depends(get_db)):
    return crud.create_item(db=db, name=name, description=description)

# Get all items
@router.get("/items", response_model=list[models.Item])
async def get_items(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_items(db=db, skip=skip, limit=limit)
