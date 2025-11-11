from fastapi import FastAPI
app= FastAPI()
@app.get('/')      #  route pour la racine
def get_lead():
    return {"message": "Bienvenue sur mon API FastAPI "}
