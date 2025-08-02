from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Camera(Base):
    __tablename__ = 'cameras'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    ip = Column(String)
    detections = relationship("Detections", back_populates="camera")

class Detections(Base):
    __tablename__ = 'detections'

    id = Column(Integer, primary_key=True)
    timestamp = Column(String)
    image_path = Column(String)
    cam_id = Column(Integer, ForeignKey('cameras.id'))
    camera = relationship("Camera", back_populates="detections")
