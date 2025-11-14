# 🎭 Détection d’Émotions Faciales  
### CNN + OpenCV + FastAPI + PostgreSQL  

### *Auteur :* __MACHAY Fatima__
### *Date :* __2025-11-14__

### *Objectif :*
Développer un prototype d’API IA capable de détecter automatiquement un visage sur une image, de prédire l’émotion faciale via un CNN (TensorFlow/Keras) et de stocker la prédiction dans une base PostgreSQL.

---
# Table des matières

1. [Objectif](#objectif)
2. [Description du projet](#description-du-projet)
   1. [Détection de visage](#détection-de-visage)
   2. [Classification des émotions](#classification-des-émotions)
   3. [API FastAPI](#api-fastapi)
       1. [POST /predict_emotion](#post-predict_emotion)
       2. [GET /history](#get-history)
   4. [Stockage PostgreSQL](#stockage-postgresql)
4. [Fonctionnalités](#fonctionnalités)
   1. [Détection automatique du visage](#détection-automatique-du-visage)
   2. [Prédiction d’émotions via CNN](#prédiction-démotions-via-cnn)
   3. [API FastAPI](#api-fastapi-1)
       1. [POST /predict_emotion](#post-predict_emotion-1)
       2. [GET /history](#get-history-1)
   4. [Base PostgreSQL](#base-postgresql)
   5. [Script OpenCV autonome](#script-opencv-autonome)
   6. [Tests](#tests)
5. [Technologies utilisées](#technologies-utilisées)
6. [Base de données PostgreSQL](#base-de-données-postgresql)

## Description du projet

Ce projet implémente un pipeline complet d’Intelligence Artificielle en Vision par Ordinateur :

- Détection de visage via **Haar Cascade (OpenCV)**
- Classification des émotions via **CNN (TensorFlow/Keras)**
- API **FastAPI** permettant de recevoir une image et prédire l’émotion
- Stockage des résultats dans **PostgreSQL**.

Ce prototype démontre la faisabilité d’un futur produit SaaS analysant les émotions d’utilisateurs (tests UX, retours clients, etc.).

---

## Fonctionnalités

### Détection automatique du visage  
Utilisation du classifieur Haar Cascade :  
`haarcascade_frontalface_default.xml`

### Prédiction d’émotions via CNN  
- Images redimensionnées en 48×48

- Dataset organisé par labels : happy/, sad/, angry/, etc.

- Prétraitements : normalisation, resizing

- Entraînement d’un modèle CNN Keras personnalisé

### API FastAPI  
Deux endpoints principaux :
#### **POST /predict_emotion**  
→ reçoit une image, détecte le visage, prédit l’émotion et enregistre la prédiction dans PostgreSQL

#### **GET /history**  
→ retourne l’historique des prédictions

### Base PostgreSQL  
 
**Table : predictions**

| Colonne       | Type    | Description                  |
|---------------|---------|------------------------------|
| id            | INT     | Clé primaire                 |
| filename      | TEXT    | Nom de l’image               |
| emotion       | TEXT    | Émotion prédite              |
| confidence    | FLOAT   | Score entre 0 et 1           |
| date_created  | DATETIME| Timestamp de l’entrée        |


###  Script OpenCV autonome  
`utiles.py` → charge le modèle, détecte, prédit et annote l’image

### Tests  
- Test du chargement du modèle  
- Test du JSON de réponse  
- Tests exécutés automatiquement à chaque commit

---

 ### Technologies utilisées


| Technologie         | Rôle              |
|---------------------|-------------------|
| Python 3.11         | Langage principal |
| TensorFlow / Keras  | Modèle CNN        |
| OpenCV              | Détection faciale |
| FastAPI             | API REST          |
| PostgreSQL          | Stockage          |
| SQLAlchemy          | ORM               |
| PyTest              | Tests             |
| Uvicorn             | Serveur ASGI      |

### Base de données PostgreSQL
Table predictions :
Colonne	Type
id	INT
filename TEXT
emotion	TEXT
confidence	FLOAT
data_created	datetime

