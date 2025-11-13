from pydantic import BaseModel
from datetime import datetime

class PredictionCreate(BaseModel):
    emotion : str
    confidence :float
class PredictionRead(BaseModel):
    id:int
    emotion: str
    confidence:float
    data_created: datetime
class configuration:
    orm_mode=True