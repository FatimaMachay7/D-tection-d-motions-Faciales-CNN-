import pytest
import cv2
import os
import numpy as np
from app.utiles import detection_picture, prediction_emotion_picture, emotion_labels

@pytest.fixture
def sample_face_image():
    path = os.path.join(os.path.dirname(__file__), "new.jpg")
    img = cv2.imread(path)
    assert img is not None, f"Image not found at {path}"
    return img
def sample_no_face_image():
    """Image vide (aucun visage)"""
    img = np.ones((100, 100, 3), dtype=np.uint8) * 255
    return img
def test_detection_face(sample_face_image):
    faces = detection_picture(sample_face_image)
    assert faces is not None
    assert len(faces) > 0


def test_prediction_emotion(sample_face_image):
    confidence, emotion = prediction_emotion_picture(sample_face_image)
    assert confidence is not None
    assert isinstance(confidence, float)
    assert emotion is not None
    assert isinstance(emotion, str)
    assert emotion in emotion_labels

