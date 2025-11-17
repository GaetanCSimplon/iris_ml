from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List

app = FastAPI()

# Définit le modèle de données d'entrées (les features)

class IrisFeatures(BaseModel):
    """ 
    Définit les 4 features attendues pour la prédiction
    """
    sepal_length: float = Field(..., examples=5.1)
    sepal_width: float = Field(..., examples=3.5)
    petal_length: float = Field(..., examples=1.4)
    petal_width: float = Field(..., examples=0.2)

# Lancement de l'API depuis un terminal : uvicorn app.main:app --reload
@app.get("/")
def root():
    """Vérifie la statut de l'API
    """
    return {"status": "ok"}

@app.post("/predict")
def predict():
    pass
    