
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship, Session
from decouple import config
from database import Base, get_db, engine, SessionLocal


DATABASE_URL = config("DATABASE_URL")

# Setup
Base = declarative_base()
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autoflush=False)


# Models
class Camera(Base):
    __tablename__ = 'camera'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    ip_address = Column(String)
    recordings = relationship("Detections", back_populates="camera")

    def __repr__(self):
        return f"Camera(ID={self.id}, Name='{self.name}', IP='{self.ip_address}')"

class Detections(Base):
    __tablename__ = 'detectors'

    id = Column(Integer, primary_key=True)
    timestamp = Column(String)
    image_path = Column(String)
    Camera_id = Column(Integer, ForeignKey('camera.id'))
    camera = relationship("Camera", back_populates="recordings")