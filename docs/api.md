# API Backend

Le backend est construit avec **FastAPI**.

## Routes

### `GET /`
Vérifie le statut de l'API.
- **Réponse** : `{"status": "ok"}`

### `POST /predict`
Prédit l'espèce d'une fleur.
- **Input** : JSON avec `sepal_length`, `sepal_width`, `petal_length`, `petal_width`.
- **Output** : JSON avec la classe prédite (ex: "setosa").