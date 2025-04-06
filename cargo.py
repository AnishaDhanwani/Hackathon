from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from services import cargo_service

router = APIRouter()

class Coordinates(BaseModel):
    width: float
    depth: float
    height: float

class Position(BaseModel):
    start_coordinates: Coordinates
    end_coordinates: Coordinates

class PlacementRequest(BaseModel):
    item_id: str
    container_id: str
    position: Position

class PlacementResponse(BaseModel):
    success: bool
    placements: List[PlacementRequest]
    rearrangements: Optional[List[dict]] = None

@router.post("/api/placement", response_model=PlacementResponse)
def placement_recommendation(items: List[dict]):
    try:
        result = cargo_service.place_cargo(items)
        return PlacementResponse(success=True, **result)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
  
