from fastapi import FastAPI, APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Camera, Detections
from database import get_db
from pydantic import BaseModel
from typing import List
import uvicorn

# Pydantic response models
class CameraResponse(BaseModel):
    id: int
    name: str
    ip: str

    class Config:
        from_attributes = True

class DetectionResponse(BaseModel):
    id: int
    timestamp: str
    image_path: str
    cam_id: int

    class Config:
        from_attributes = True

# Create router
router = APIRouter()

@router.get("/")
def index():
    return {"message": "API is running"}

@router.get("/cameras", response_model=List[CameraResponse])
def get_all_cameras(db: Session = Depends(get_db)):
    return db.query(Camera).all()


@router.get("/camera/{id}", response_model=CameraResponse)
def get_camera_by_id(id: int, db: Session = Depends(get_db)):
    camera = db.query(Camera).filter(Camera.id == id).first()
    if camera is None:
        raise HTTPException(status_code=404, detail="Camera not found for this id")
    return camera

@router.get("/camera/{id}/detections", response_model=List[DetectionResponse])
def get_detections_by_camera_id(id: int, db: Session = Depends(get_db)):
    detections = db.query(Detections).filter(Detections.cam_id == id).all()
    
    # Convert timestamps to string (e.g., "17:43:57")
    response = []
    for det in detections:
        det_dict = {
            "id": det.id,
            "timestamp": det.timestamp.strftime("%H:%M:%S"),  # convert time to string
            "image_path": det.image_path,
            "cam_id": det.cam_id
        }
        response.append(det_dict)
    
    return response

@router.get("/detections", response_model=List[DetectionResponse])
def get_all_detections(db: Session = Depends(get_db)):
    return db.query(Detections).all()

# Create FastAPI app and include the router
app = FastAPI()
app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)