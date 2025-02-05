from pydantic import BaseModel

class DetectionBase(BaseModel):
    x1: float
    y1: float
    x2: float
    y2: float
    confidence: float
    class_label: str

class DetectionCreate(DetectionBase):
    pass

class Detection(DetectionBase):
    id: int

    class Config:
        orm_mode = True
