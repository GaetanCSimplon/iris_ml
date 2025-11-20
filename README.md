# Iris ML - Pipeline CI/CD

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Compose-2496ED?logo=docker&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?logo=fastapi)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white)
![Azure](https://img.shields.io/badge/Microsoft_Azure-0078D4?logo=microsoft-azure&logoColor=white)

##  Objectif
Ce projet est une démonstration **MLOps** complète.
Il permet de prédire l'espèce d'une fleur d'Iris via une interface web, en utilisant un modèle de Machine Learning conteneurisé et déployé automatiquement via un pipeline CI/CD.

## Version déployée (Microsoft Azure)

[Iris ML](https://iris-ml-front-f8djewduezbehwe3.francecentral-01.azurewebsites.net/)

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

## Diagramme de séquence

```mermaid
sequenceDiagram
    actor User as "Utilisateur"
    participant Front as "Frontend Streamlit"
    participant Back as "Backend FastAPI"
    participant Model as "Modèle ML pkl"

    User->>Front: Accès à l’interface web
    activate Front
    Front->>User: Affiche le formulaire Iris

    User->>Front: Saisie des mesures et clic sur Prédire
    Front->>Back: POST /predict (JSON)
    activate Back

    Back->>Model: Chargement et exécution du modèle
    activate Model
    Model-->>Back: Classe prédite
    deactivate Model

    Back-->>Front: Réponse HTTP 200 (JSON)
    deactivate Back

    Front->>User: Affiche le résultat
    deactivate Front

```

## Interactions

```mermaid
flowchart TD
    classDef script fill:#e1f5fe,stroke:#01579b,stroke-width:2px
    classDef file fill:#fff9c4,stroke:#fbc02d,stroke-width:2px,stroke-dasharray:5 5
    classDef http fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px

    subgraph Machine_Learning["Phase 1 : Entrainement"]
        TrainScript["backend/ml/train.py"]:::script
    end

    subgraph Stockage["Phase 2 : Persistance"]
        ModelPKL["backend/model/model.pkl"]:::file
    end

    subgraph Execution["Phase 3 : Runtime Docker"]
        direction TB
        API["backend/app/api.py"]:::script
        UI["frontend/app.py"]:::script
        User(("Utilisateur"))
    end

    TrainScript -->|"1. Genere et sauvegarde"| ModelPKL
    ModelPKL -.->|"2. Charge au demarrage"| API

    User -->|"3. Interagit avec"| UI
    UI -->|"4. Envoie requete HTTP JSON"| API
    API -->|"5. Utilise le modele pour predire"| ModelPKL
    API -->|"Reponse JSON"| UI


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

## Bonus : Azure ML Tracking (branche ml_azure_tracking)

Le tracking des expériences est configuré pour fonctionner avec **Azure Machine Learning**.

**Note technique :**
L'automatisation complète de l'entraînement via GitHub Actions nécessiterait la création d'un *Service Principal* Azure.
En raison des restrictions de permissions sur le compte étudiant (droits Active Directory limités), cette étape n'a pas pu être implémentée dans le CI/CD.

Cependant, le tracking fonctionne parfaitement en **lancement local authentifié** (`az login`), permettant de centraliser les logs d'expérience sur le cloud Azure.

[Lien Azure ML - Iris ML](https://ml.azure.com/?wsid=/subscriptions/fbf86e5f-ad89-41dd-bcc2-4fb5e64140b0/resourceGroups/gcourtieuRG/providers/Microsoft.MachineLearningServices/workspaces/Iris-ML&tid=a2e466aa-4f86-4545-b5b8-97da7c8febf3)

**Fonctionnement**

```mermaid
flowchart TD
    subgraph VS_Code["Votre Ordinateur WSL"]
        Script["Script train.py"]
        EnvVar["Variable : MLFLOW_TRACKING_URI"]
        Auth["Session : az login - votre compte"]
    end

    subgraph Azure_Cloud["Microsoft Azure"]
        AzureML["Azure Machine Learning"]
        Metrics["Graphiques et Logs"]
        Artifacts["Modele .pkl"]
    end

    Script -->|1. Verifie| EnvVar
    EnvVar -->|"Existe ?"| OUI
    OUI{"Oui"} -->|2. Utilise| Auth
    Auth -->|3. Envoie donnees via internet| AzureML

    AzureML --> Metrics
    AzureML --> Artifacts

    classDef azure fill:#007fff,stroke:#fff,color:#fff,stroke-width:2px
    class AzureML,Metrics,Artifacts azure



```

