from basedata import Base, engine
from models import Emotionprediction

print("Création des tables..")
Base.metadata.create_all(bind=engine)
print(" Tables créées avec succès.")