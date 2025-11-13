import tensorflow as tf
import cv2
import numpy as np
import os
from tensorflow.keras.models import load_model



# Charger le classifieur Haar Cascade :
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)
print(cv2.data.haarcascades)
# Charger le modèle CNN :
model = tf.keras.models.load_model("Model_CNN_faces.keras")
# Les classes (émotions) :
emotion_labels = ['angry', 'disgusted', 'fearful', 'happy', 'neutral', 'sad', 'surprised']
# Les fonctions de traitement_prediction :
def detection_picture(img) :
    gray=cv2.cvtColor(img, cv2.COLOR_BAYER_BG2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1,5)
    return faces
def prediction_emotion_picture(img) :
    faces=detection_picture(img)
    if len(faces)==0:
        return None, None
    x,y,w,h= faces[0]
    face_img= cv2.resize(img[y :y+h, x: x+w],(48,48))
    face_img = face_img / 255.0
    if face_img.ndim== 2 :
          face_img = np.expand_dims(face_img, axis=-1)
    face_img = np.repeat(face_img, 3, axis=-1)
    face_img = np.expand_dims(face_img, axis=0) # convertir en 3 canaux
    prediction = model.predict(face_img)
    emotion_index = np.argmax(prediction)
    emotion = emotion_labels[emotion_index]
    confidence=float(np.max(prediction))
    return confidence, emotion