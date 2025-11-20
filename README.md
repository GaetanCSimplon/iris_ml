# Iris MLOps

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Compose-2496ED?logo=docker&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?logo=fastapi)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white)

##  Objectif
Ce projet est une démonstration **MLOps** complète.
Il permet de prédire l'espèce d'une fleur d'Iris via une interface web, en utilisant un modèle de Machine Learning conteneurisé et déployé automatiquement via un pipeline CI/CD.

## Architecture
Le projet fonctionne en **micro-services** orchestrés par Docker :

```
iris-ml/
├── .github/
│   └── workflows/
│       └── main.yml         # Pipeline CI/CD (GitHub Actions)
│
├── backend/                 # Service API & Machine Learning
│   ├── app/
│   │   ├── __init__.py
│   │   └── api.py           # Code de l'API (FastAPI)
│   ├── ml/
│   │   └── train.py         # Script d'entraînement du modèle (Via MLflow)
│   ├── model/
│   │   └── model.pkl        # Le modèle entraîné (Artefact, issu de MLflow)
│   ├── tests/
│   │   ├── __init__.py
│   │   └── test_api.py      # Tests unitaires (Pytest)
│   ├── Dockerfile           # Instruction de build pour l'image Backend
│   └── requirements.txt     # Dépendances (FastAPI, scikit-learn...)
│
├── frontend/                # Service Interface Utilisateur
│   ├── app.py               # Application Streamlit
│   ├── Dockerfile           # Instruction de build pour l'image Frontend
│   └── requirements.txt     # Dépendances (Streamlit, requests)
│
├── docs/                    # Sources de la documentation (Markdown)
├── docker-compose.yml       # Orchestration des conteneurs (Local)
├── mkdocs.yml               # Configuration du site de documentation
└── .gitignore               # Fichiers ignorés par Git (.venv, secrets...)
```

## Installation

Prérequis: Docker Desktop et Git

```bash
git clone https://github.com/GaetanCSimplon/iris_ml.git
cd iris_ml
```

## Lancement

- Méthode make

```bash
make run
```

- Methode Docker

```bash
docker compose up --build
```

## Accès

Une fois lancé, ouvrez votre navigateur :
- Application : http://localhost:8501
- Documentation API : http://localhost:8000/docs

## Documentation 

https://gaetancsimplon.github.io/iris_ml/


