# Détection d’émotions faciales  
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
5. [Intégration continue avec GitHub Actions](#Intégration-continue-avec-GitHub-Actions)
6. [Technologies utilisées](#technologies-utilisées)
7. [Base de données PostgreSQL](#base-de-données-postgresql)
8. [Contribuer](#contribuer)
9. [Contact](#contact)

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

<div align="center">

| __Colonne__   | __Type__| __Description__              |
|---------------|---------|------------------------------|
| id            | INT     | Clé primaire                 |
| filename      | TEXT    | Nom de l’image               |
| emotion       | TEXT    | Émotion prédite              |
| confidence    | FLOAT   | Score entre 0 et 1           |
| date_created  | DATETIME| Timestamp de l’entrée        |

</div>

###  Script OpenCV autonome  
`utiles.py` → charge le modèle, détecte, prédit et annote l’image

### Tests  
- Test du chargement du modèle  
- Test du JSON de réponse  
- Tests exécutés automatiquement à chaque commit

#### Intégration continue avec GitHub Actions
Les tests sont exécutés automatiquement à chaque push ou pull request sur la branche main grâce à l’intégration continue via GitHub Actions. 
---

 ### Technologies utilisées

<div align="center">

| __Technologie__     | __Rôle__          |
|---------------------|-------------------|
| Python 3.11         | Langage principal |
| TensorFlow / Keras  | Modèle CNN        |
| OpenCV              | Détection faciale |
| FastAPI             | API REST          |
| PostgreSQL          | Stockage          |
| SQLAlchemy          | ORM               |
| PyTest              | Tests             |
| Uvicorn             | Serveur ASGI      |

</div>

### Base de données PostgreSQL

**Table : predictions**

<div align="center">

| __Colonne__    | __Type__ |
|---------------|-----------|
| id            | INT       |
| filename      | TEXT      |
| emotion       | TEXT      |
| confidence    | FLOAT     |
| date_created  | DATETIME  |

</div>

## Contribuer :

Les contributions sont les bienvenues ! Si vous trouvez un bug ou souhaitez améliorer le projet, n’hésitez pas à forker le dépôt et soumettre une demande de pull.
Pour contribuer :
- Forkez le dépôt.
- Créez une nouvelle branche.
- Effectuez vos modifications.
- Soumettez une demande de pull.

## Contact :

_N'hésitez pas à me contacter en cas de problème ou si vous avez des questions.
Email : [fatimamachay5@gmail.com]_
