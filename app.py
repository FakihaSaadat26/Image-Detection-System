
from fastapi import FastAPI, APIRouter, Depends
from sqlalchemy.orm import Session
from models import get_db, Camera, Detections
from pydantic import BaseModel
from typing import List


# Pydantic response models
class CameraResponse(BaseModel):
    id: int
    name: str
    ip_address: str

    class Config:
        orm_mode = True

class DetectionResponse(BaseModel):
    id: int
    timestamp: str
    image_path: str
    Camera_id: int

    class Config:
        orm_mode = True

# Create router
router = APIRouter()

@router.get("/")
def index():
    return {"message": "API is running"}

@router.get("/camera", response_model=List[CameraResponse])
def get_camera(db: Session = Depends(get_db)):
    return db.query(Camera).all()

@router.get("/detection", response_model=List[DetectionResponse])
def get_detection(db: Session = Depends(get_db)):
    return db.query(Detections).all()

# Create FastAPI app and include the router
app = FastAPI()
app.include_router(router)