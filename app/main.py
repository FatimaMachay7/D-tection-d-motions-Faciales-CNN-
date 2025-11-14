from fastapi import FastAPI, UploadFile, File, HTTPException, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from basedata import sessionlocal, engine, Base
from models import Emotionprediction
from datetime import datetime
from utiles import prediction_emotion_picture
from schemas import PredictionCreate, PredictionRead
from basedata import get_db
import tensorflow as tf
import cv2
import numpy as np
import shutil
import os
app= FastAPI(Title="Détection d'émotions")
@app.get('/')      #  route pour la uviracine
def get_lead():
    return {"message": "Bienvenue "}
UPLOAD_DIRECTORY="temp"
os.makedirs(UPLOAD_DIRECTORY,exist_ok=True)

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

model = tf.keras.models.load_model("Model_CNN_faces.keras")

emotion_labels = ['angry', 'disgusted', 'fearful', 'happy', 'neutral', 'sad', 'surprised']

@app.post ("/prediction_emotion")
async def prediction_emotion(file: UploadFile=File(...),db:Session= Depends(get_db)):
# Lecture du fichier image envoyé par le client
    contents=await file.read()
    nparr=np.frombuffer(contents,np.uint8)
    img=cv2.imdecode(nparr,cv2.IMREAD_COLOR)
  # Prédiction de l'émotion :
    confidence, emotion = prediction_emotion_picture(img)
    if emotion is None:
        return {"message": "Aucun visage détecté sur l'image."}
# Enregistrement dans la base de données
    record = Emotionprediction(
        filename=file.filename,
        emotion=emotion,
        confidence=confidence
    )
    db.add(record)
    db.commit()
# Réponse JSON
    return {
        "filename": file.filename,
        "emotion": emotion,
        "confidence": confidence
    }
from fastapi import HTTPException

@app.post("/prediction_emotions_faces", response_model=PredictionRead)
async def prediction_emotion(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):

    try:
        # Lecture du fichier image
        contents = await file.read()
        nparr = np.frombuffer(contents, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        # Prédiction
        confidence, emotion = prediction_emotion_picture(img)

        if emotion is None:
            raise HTTPException(status_code=400, detail="Aucun visage détecté.")

        # Enregistrement dans la base
        record = Emotionprediction(
            filename=file.filename,
            emotion=emotion,
            confidence=confidence
        )

        db.add(record)
        db.commit()

        return record

    except Exception as e:
        db.rollback()   # ⛔ IMPORTANT : annule la transaction si erreur
        raise HTTPException(
            status_code=500,
            detail=f"Erreur lors de l'enregistrement dans la base : {str(e)}"
        )

# Endpoint : historique des prédictions

@app.get("/history/", response_model=list[PredictionRead])
def get_history(db: Session = Depends(get_db)):
    """
    Retourne l'historique des prédictions stockées en base.
    """
    records = db.query(Emotionprediction).all()
    return records