from fastapi import APIRouter, UploadFile, File
from fastapi.responses import JSONResponse

router = APIRouter()

@router.post("/api/waste/identify")
async def identify_waste(file: UploadFile = File(...)):
    
    contents = await file.read()
    size_kb = len(contents) / 1024
    return JSONResponse(content={"filename": file.filename, "size_kb": round(size_kb, 2)})



from fastapi import APIRouter

router = APIRouter()

@router.get("/waste/return-plan")
def generate_return_plan():
    
    return {
        "plan": [
            {"item_id": "item123", "action": "return to Earth", "container": "C-42"},
            {"item_id": "item456", "action": "dispose via incineration", "container": "C-12"},
        ]
    }
