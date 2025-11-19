# Architecture du projet


```text
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