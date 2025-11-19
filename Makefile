# .PHONY dit à Make : "Ces noms sont des commandes, pas des fichiers"
.PHONY: docs api run

# Lance la documentation sur le port 8001
docs:
	mkdocs serve -a localhost:8001

# Lance l'API en local
api:
	cd backend && .venv/bin/uvicorn app.api:app --reload

# Lance tout avec Docker
run:
	docker compose up --build