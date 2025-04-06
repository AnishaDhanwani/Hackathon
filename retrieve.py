# routes/retrieve.py

from fastapi import APIRouter

router = APIRouter()  # REMOVE prefix="/api"

@router.get("/retrieve")
def retrieve_items():
    return {"items": ["item1", "item2"]}

