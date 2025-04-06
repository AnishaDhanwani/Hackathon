from fastapi import APIRouter

router = APIRouter()

@router.get("/api/search")
async def search_items():
    return {"message": "Search endpoint is working"}
