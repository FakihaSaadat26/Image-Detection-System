from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define your PostgreSQL connection URL
# Replace with your actual credentials
DATABASE_URL = "postgresql+psycopg2://username:password@localhost:5432/your_database"

# Setup
Base = declarative_base()
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()


class Camera(Base):
    __tablename__ = 'camera'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    ip_address = Column(String)

class Detections(Base):
    __tablename__ = 'detectors'

    id = Column(Integer, primary_key=True)
    timestamp = Column(String)
    image_path = Column(String)
    Camera_id = Column(Integer,ForeignKey('camera.id'))

camera = relationship("Camera", back_populates="recordings")
    

def __repr__(self):
        return f"Camera(ID={self.id}, Name='{self.name}', IP='{self.ip_address}')"

# Create the table (run this once)
def create_tables():
    Base.metadata.create_all(engine)

# Fetch all cameras
def fetch_all_cameras():
    cameras = session.query(Camera).all()
    return cameras

# Fetch camera by ID
def fetch_camera_by_id(camera_id):
    return session.query(Camera).filter_by(id=camera_id).first()

# Example usage
if __name__ == "__main__":
    # create_tables()  # Uncomment if table not created yet

    print("All Cameras:")
    for cam in fetch_all_cameras():
        print(cam)

    print("\nCamera with ID 2:")
    cam = fetch_camera_by_id(2)
    print(cam if cam else "Not found")