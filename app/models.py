from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, Float
from basedata import Base, engine
from datetime import datetime

class Emotionprediction(Base) :
    __tablename__= 'predictions'
    id= Column(Integer, primary_key=True, index=True)
    filename = Column(String, nullable=True)  # ← IMPORTANT !!!
    emotion=Column(String, index=True)
    confidence= Column(Float, nullable=False)    # non, elle ne peut pas être vide.
    data_created =Column(DateTime, default= datetime.utcnow)
Base.metadata.create_all(bind=engine)

