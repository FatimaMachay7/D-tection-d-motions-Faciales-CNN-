from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from basedata import sessionlocal, engine, Base
from models import Emotionprediction
from datetime import datetime
import tensorflow as tf
import numpy as np
import cv2
import io

app= FastAPI()
@app.get('/')      #  route pour la racine
def get_lead():
    return {"message": "Bienvenue "}
# Charger le modéle de CNN :
model = tf.keras.models.load_model("Model_CNN_faces.keras")
# # Cascade de détection de visages :
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

emotion_labels = ['angry', 'disgusted', 'fearful', 'happy', 'neutral', 'sad', 'surprised']
