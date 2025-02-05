from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/detections/", response_model=schemas.Detection)
def create_detection(detection: schemas.DetectionCreate, db: Session = Depends(get_db)):
    return crud.create_detection(db=db, detection=detection)

@app.get("/detections/", response_model=list[schemas.Detection])
def read_detections(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    detections = crud.get_detections(db, skip=skip, limit=limit)
    return detections

@app.get("/detections/{detection_id}", response_model=schemas.Detection)
def read_detection(detection_id: int, db: Session = Depends(get_db)):
    db_detection = crud.get_detection(db, detection_id=detection_id)
    if db_detection is None:
        raise HTTPException(status_code=404, detail="Detection not found")
    return db_detection
