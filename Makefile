.DEFAULT_GOAL := help
.SILENT:
.PHONY: help

## Docker
BACKEND_DOCKER_CONTAINER = api

## 🎨 Couleurs
COLOR_RESET   = \033[0m
COLOR_INFO    = \033[32m
COLOR_COMMENT = \033[33m
COLOR_SECTION = \033[36m

## 🆘 Affiche cette aide
help:
	printf "${COLOR_COMMENT}Usage:${COLOR_RESET}\n"
	printf "  make [commande]\n\n"
	printf "${COLOR_COMMENT}Commandes disponibles :${COLOR_RESET}\n"
	awk ' \
		BEGIN { section = "" } \
		/^\#\# \[.*\]/ { \
			section = substr($$0, 5, length($$0) - 5); \
			printf "\n${COLOR_SECTION}🧩  %s${COLOR_RESET}\n", section; \
			next; \
		} \
		/^\#\# [^[]/ { \
			desc = substr($$0, 4); \
			next; \
		} \
		/^[^.#][a-zA-Z0-9\-_\.@]+:/ { \
			cmd = substr($$1, 0, length($$1)-1); \
			printf "  ${COLOR_INFO}%-20s${COLOR_RESET} %s\n", cmd, desc; \
			desc = ""; \
		} \
	' COLOR_SECTION=$(COLOR_SECTION) COLOR_RESET=$(COLOR_RESET) COLOR_INFO=$(COLOR_INFO) $(MAKEFILE_LIST)

## [ENV]
## 🔧 Crée le fichier .env
env:
	if [ ! -f .env ]; then cp .env.example .env; fi
	@echo "${COLOR_RESET}Fichier .env créé !${COLOR_RESET}"
	@echo "N'oubliez pas de le remplir !"
	@echo "${COLOR_COMMENT}Le fichier se trouve dans 1Passowrd !${COLOR_RESET}"

## [DOCKER]
## 🔨 Build des containers Docker
build:
	@echo "${COLOR_INFO}Build du projet...${COLOR_RESET}"
	docker-compose build

## 🚀 Démarre le serveur de développement
start:
	@echo "${COLOR_INFO}Démarrage du serveur...${COLOR_RESET}"
	docker-compose up -d

## 🛑 Stoppe le serveur
stop:
	@echo "${COLOR_INFO}Arrêt du serveur...${COLOR_RESET}"
	docker-compose down

## 🔄 Redémarre le serveur
restart: stop build start

## 📜 Affiche les logs
logs:
	docker-compose logs -f

## [Migrations]
## 🛠 Crée une nouvelle migration
migration-new:
	@echo "${COLOR_INFO}Création d'une nouvelle migration...${COLOR_RESET}"
	docker-compose run --rm ${BACKEND_DOCKER_CONTAINER} python manage.py db migrate -m "$(name)"

## 📥 Applique les migrations
migration-migrate:
	docker-compose run --rm ${BACKEND_DOCKER_CONTAINER} python manage.py db upgrade

## ⏪ Restaure la migration précédente
migration-rollback:
	docker-compose run --rm ${BACKEND_DOCKER_CONTAINER} python manage.py db downgrade

## 📚 Affiche l’historique des migrations
migration-history:
	docker-compose run --rm ${BACKEND_DOCKER_CONTAINER} python manage.py db history

## 🔎 Affiche la version actuelle
migration-current:
	docker-compose run --rm ${BACKEND_DOCKER_CONTAINER} python manage.py db current

## [Scripts]
## ➡️ Crée un nouveau modèle
create-model:
	docker-compose run --rm ${BACKEND_DOCKER_CONTAINER} python scripts/make/model.py

## ➡️ Crée une nouvelle route
create-route:
	docker-compose run --rm ${BACKEND_DOCKER_CONTAINER} python scripts/make/route.py

## [Qualité]
## 🧼 Lint du code avec flake8
lint:
	docker-compose run --rm backend flake8 app scripts tests

## 🧽 Formatte le code avec black + isort
format:
	docker-compose run --rm backend sh -c "isort . && black ."
