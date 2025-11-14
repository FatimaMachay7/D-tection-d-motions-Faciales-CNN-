from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class PredictionCreate(BaseModel):
    emotion : str
    confidence :float

class PredictionRead(BaseModel):
    filename: Optional[str]
    emotion: str
    confidence: float
    data_created: datetime | None = None

    class Config:
        orm_mode = True