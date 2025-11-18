import pytest
import os
from fastapi.testclient import TestClient
import sys

# Chemin vers le dossier app/ contenant le fichier api.py
APP_DIR = os.path.dirname(os.path.abspath(__file__))
BACKEND_DIR = os.path.normpath(os.path.join(APP_DIR, ".."))
sys.path.append(BACKEND_DIR)

from app.api import app

client = TestClient(app)

# Route "status"
def test_get_status():
    """ 
    Teste si la route GET renvoie bien un status 200 OK et le bon message JSON.
    """
    # Simulation d'une requête GET vers /
    response = client.get("/")
    
    # Vérification que la status code = 200 (OK)
    assert response.status_code == 200
    # Vérification que le contenu JSON = {"status": "ok"}
    assert response.json() == {"status": "ok"}

# Route "predict"
def test_post_predict_stetosa():
    """ 
    Teste si la route POST /predict renvoie la bonne prédiction pour une fleur Iris Setosa connue.
    """
    # Données d'une Steosa (Sepal 5.1, 3.5; Petal 1.4, 0.2)
    test_data = {
        "sepal_length": 5.1,
        "sepal_width": 3.5,
        "petal_length": 1.4,
        "petal_width": 0.2
    }
    
    # Simulation d'une requête POST vers /predict avec le test_data
    response = client.post("/predict", json=test_data)
    # Vérification du status_code
    assert response.status_code == 200
    # Récupération de la réponse
    response_json = response.json()
    
    # Vérification de la prediction de classe (numérique) et du nom de la classe (nominatif)
    assert response_json["prediction"] == 0
    assert response_json["prediction_class"] == "setosa"

# Test de levée d'erreur
def test_post_predict_invalid_input():
    """ 
    Teste si l'API renvoie bien une erreur 422 (Unprocessable Entity)
    quand les données d'entrée sont invalides (ex: chemin manquant).
    """
    invalid_data = {
        "sepal_length": 5.1,
        "sepal_width": 3.5,
        "petal_length": 1.4
    }
    # Simulation d'une requête POST
    response = client.post("/predict", json=invalid_data)
    
    # Vérification du status_code 422
    assert response.status_code == 422
    