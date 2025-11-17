import pandas as pd
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score
import mlflow
import joblib 
import os


# 1. Obtenir le chemin absolu du dossier où se trouve ce script (backend/ml)
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# 2. Construire le chemin vers le dossier 'model' (qui est dans backend/)
# os.path.join(SCRIPT_DIR, "..") -> remonte à 'backend/'
# os.path.join(..., "model") -> descend dans 'model/'
MODEL_DIR = os.path.join(SCRIPT_DIR, "..", "model")

# 3. Normaliser le chemin (enlève les ".." inutiles)
MODEL_DIR = os.path.normpath(MODEL_DIR)

# 4. Créer le dossier s'il n'existe pas
os.makedirs(MODEL_DIR, exist_ok=True)

# 5. Définir le chemin final de notre modèle de production
MODEL_PATH = os.path.join(MODEL_DIR, "model.pkl")
# --- Fin de la gestion des chemins ---


# Création de l'expériment
mlflow.set_experiment("Iris ML")

# Load the Iris dataset
X, y = datasets.load_iris(return_X_y=True)

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Define the model hyperparameters
params = {
    "solver": "lbfgs",
    "max_iter": 1000,
    "random_state": 8888,
}

# Enable autologging for scikit-learn
mlflow.sklearn.autolog()

with mlflow.start_run():
    
    # Train model
    lr = LogisticRegression(**params)
    lr.fit(X_train, y_train)
    
    # Prédiction et scores
    y_pred = lr.predict(X_test)
    
    # Correction de l'erreur F1-score
    accuracy = accuracy_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred, average='macro')
    
    print(f"Accuracy : {accuracy}")
    print(f"F1-score (macro) : {f1}")
    
    # --- SAUVEGARDE DU MODÈLE (Simple et Robuste) ---
  
    joblib.dump(lr, MODEL_PATH)
    print(f"Modèle de production sauvegardé dans : {MODEL_PATH}")