# 🍭 SugarFree — Backend

Bienvenue dans le projet **SugarFree** : une application mobile d’aide au sevrage du sucre.  
Ce dépôt contient le **backend en Flask**, conçu pour fonctionner via **Docker** et contrôlé avec un **Makefile** simplifié.

---

## 🚀 Fonctionnalités du backend

- API RESTful avec Flask
- Authentification JWT
- Base PostgreSQL
- Migrations Alembic
- Schémas de validation Marshmallow
- Architecture modulaire
- Scripts pour générer modèles/routes/tests
- Déploiement via Docker et Portainer

---

## 📦 Prérequis

Pour développer ou lancer l'application, tu auras besoin des outils suivants :

| Outil         | Rôle                            |
|---------------|---------------------------------|
| Docker        | Conteneurisation de l'app       |
| Docker Compose| Lancement multi-services        |
| Make          | Interface CLI simplifiée         |
| Python 3.11+  | Pour les scripts (hors Docker)  |

---

## 💻 Installation par système

<details>
    <summary>macOS (via Homebrew)</summary>

```bash
brew install docker
brew install make
brew install python@3.11
```

Assure-toi que Docker Desktop est bien lancé.
</details>

<details>
<summary>Linux (Ubuntu / Debian)</summary>

```bash
sudo apt update
sudo apt install docker.io docker-compose make python3.11 python3.11-venv -y
pip3 install pre-commit
sudo usermod -aG docker $USER
newgrp docker
```

⚠️ Redémarre ta session ou fais newgrp docker pour que Docker fonctionne sans sudo.
</details>

<details>
    <summary>Windows</summary>

1.	Installe Docker Desktop
2.	Active WSL 2 (si demandé)
3.	Installe Make avec Chocolatey:
```bash
choco install make
```
4. Installe Python 3.11 via le site officiel
5. Installe  pre-commit
```bash
pip install pre-commit
```

</details>


Ensuite installer les dépendances local pip de développement
```bash
pip install -r requirements-dev.txt
```

---

## 🛠️ Lancer le projet

1. Faite en premier la commande: `make env`

2. Construiser l'image docker et lancer là, voici des commande utiles
```bash
# Build du projet
make build

# Lancer les containers
make start

# Afficher les logs
make logs

# Arrêter le projet
make stop
```

---

## 🔄 Migrations de base de données

```bash
# Créer une migration
make migration-new name="CreateUser"

# Appliquer les migrations
make migration-migrate

# Voir les versions
make migration-current
```

---

## 🧰 Générateurs de code

```bash
# Créer un modèle interactif
make create-model

# Créer une route
make create-route
```

---

## 🧷 Hooks Pre-Commit

```bash
pip install pre-commit         # Installe le binaire
pre-commit install             # Active les hooks
pre-commit run --all-files     # Exécute manuellement
```

Les hooks incluent:
- black (formatage)
- isort (imports)
- flake8 (linting)

---

## 📂 Structure du projet

Voir [docs/STRUCTURE.md](./docs/Structure.md) pour une vue complète des dossiers.

---

## 🤝 Contribuer

Ce projet est pensé comme un outil pédagogique aussi.
N’hésite pas à créer des issues, des pull requests ou poser des questions 🙌

---

## 🧠 À propos

Ce backend fait partie du projet SugarFree Challenge, une application mobile pour accompagner les utilisateurs dans leur sevrage du sucre, avec système de niveaux, compteurs, notifications et recettes saines.
