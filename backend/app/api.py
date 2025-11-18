from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List
import logging
import joblib
import os

# CONFIGURATION DU LOGGING
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# CHARGEMENT DU MODELE
APP_DIR = os.path.dirname(os.path.abspath(__file__))
BACKEND_DIR = os.path.normpath(os.path.join(APP_DIR, ".."))
MODEL_PATH = os.path.join(BACKEND_DIR, "model", "model.pkl")

model = None

try:
    model = joblib.load(MODEL_PATH)
    logger.info(f"Modèle chargé avec succès depuis : {MODEL_PATH}")
except FileNotFoundError:
    logger.info(f"ERREUR : Fichier modèle non trouvé à {MODEL_PATH}")
except Exception as e:
    logger.error(f"ERREUR : Echec du chargement du modèle. {e}")

app = FastAPI()

# Définit le modèle de données d'entrées (les features)


class IrisFeatures(BaseModel):
    """
    Définit les 4 features attendues pour la prédiction
    """

    sepal_length: float = Field(..., examples=[5.1])
    sepal_width: float = Field(..., examples=[3.5])
    petal_length: float = Field(..., examples=[1.4])
    petal_width: float = Field(..., examples=[0.2])


# Lancement de l'API depuis un terminal : uvicorn app.api:app --reload
@app.get("/")
def root():
    """Vérifie la statut de l'API"""
    return {"status": "ok"}


@app.post("/predict")
def predict(features: IrisFeatures):
    """
    Prédit la classe d'une fleur Iris à partir de ses features
    """
    # Vérification du chargement du modèle
    if model is None:
        logger.warning("Appel à /predict mais modèle non chargé.")
        return {"error": "Modèle non disponible"}, 503
    logger.info(f"Appel à /predict avec les features : {features.model_dump()}")

    try:
        # Formatage des features
        input_data = [
            [
                features.sepal_length,
                features.sepal_width,
                features.petal_length,
                features.petal_width,
            ]
        ]
        # Prédiction
        prediction_array = model.predict(input_data)
        logger.info(f"Classe prédite : {prediction_array}")
        # Extraction du résultat
        prediction_value = int(prediction_array[0])
        logger.info(f"Valeur extraite : {prediction_value}")
        # Nom de la classe
        class_names = ["setosa", "versicolor", "virginica"]
        prediction_class = class_names[prediction_value]

        logger.info(f"Prédiction : {prediction_class} {prediction_value}")

        return {"prediction": prediction_value, "prediction_class": prediction_class}
    except Exception as e:
        logger.error(f"Erreur durant la prédiction : {e}")
