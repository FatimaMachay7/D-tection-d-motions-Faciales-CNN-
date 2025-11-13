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

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)

model = tf.keras.models.load_model("Model_CNN_faces.keras")

emotion_labels = ['angry', 'disgusted', 'fearful', 'happy', 'neutral', 'sad', 'surprised']

@app.post ("/prediction_emotion", response_model=PredictionRead)
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
# Endpoint : historique des prédictions
# =============================
@app.get("/history/")
def get_history(db: Session = Depends(get_db)):
    """
    Retourne l'historique des prédictions stockées en base.
    """
    records = db.query(Emotionprediction).all()
    return [
        {"filename": r.filename, "emotion": r.emotion, "confidence": r.confidence}
        for r in records
    ]


# =============================
# ▶️ Lancer le serveur (facultatif si tu utilises uvicorn en ligne de commande)
# =============================
# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)