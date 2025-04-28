# 📦 Structure du projet backend — SugarFree

Ce backend utilise **Flask** et suit une architecture modulaire claire, adaptée à une application mobile connectée via une API REST.  
L’objectif est de séparer les responsabilités pour faciliter la maintenance, les tests et les évolutions.

---

## 🗂️ Arborescence
```
backend/
├── app/                 # Code source principal de l’application Flask
│   ├── init.py          # Point d’entrée Flask : create_app()
│   ├── config.py        # Configuration (prod, dev, test)
│   ├── db/              # Connexion base de données & modèles
│   │   ├── init.py      # Objet SQLAlchemy “db”
│   │   └── migrations/  # Migrations Alembic
│   ├── models/          # Modèles SQLAlchemy (ex : User, Motivation)
│   ├── schemas/         # Schémas Marshmallow (validation / sérialisation)
│   ├── routes/          # Blueprints Flask = endpoints API REST
│   ├── services/        # Logique métier réutilisable (ex : auth, notifications)
│   └── utils/           # Fonctions utilitaires diverses
│
├── scripts/             # Scripts CLI personnalisés
│   └── make/
│           ├── model.py # Génère un modèle + schéma interactif
│           ├── test.py  # Génère un test de base pour une entité
│           └── ect ...
│
├── tests/               # Tests unitaires (pytest)
│   └── test_*.py        # Un test par entité ou fonctionnalité
│
├── docs/                # Dossiers contenant la documentations developpeur
│   └── *.md             # Fichier contenant une documentation spécifié par son nom
│
├── Dockerfile           # Image Docker de prod
├── docker-compose.yml   # Environnement de dev multi-service
├── manage.py            # Point d’entrée CLI (runserver, create-db, etc.)
├── requirements.txt     # Dépendances de production
├── requirements-dev.txt # Dépendances pour le développement (tests, outils, etc.)
├── .env                 # Variables d’environnement locales (non versionné)
├── .env.exemple         # Fichier des variables d’environnement locales (exemple sans donnée)
├── Makefile             # Fichier permettant de créer des commande facile et utilisable rapidement
└── README.md            # Informations sur le projets
```

---

## 🧪 Tests

- Les tests sont basés sur `pytest` avec `pytest-flask`.
- On place un fichier `test_<entité>.py` par module logique dans le dossier `tests/`.
- On utilise des **fixtures** pour initialiser des clients de test ou la base.

---

## 🛠️ Scripts CLI (type "Symfony Maker")

Les scripts du dossier `scripts/make/` permettent de générer automatiquement du code :

- `model.py` : pose des questions pour créer un modèle SQLAlchemy + schéma Marshmallow.
- `test.py` : crée un fichier de test unitaire de base pour une entité.

Ces outils visent à faciliter le travail des développeurs, notamment les profils junior, en évitant le code répétitif et les oublis.

---

## 📚 Bonnes pratiques

- Chaque modèle a un schéma dédié pour la validation/sérialisation.
- On isole la logique métier dans `services/`.
- Chaque route est un **Blueprint** dans `routes/`.
- La base est modulaire, documentée, extensible.

---

## 🔧 Commandes utiles

```bash
# Lancer l'app en dev via Docker
docker-compose up --build -d

# Générer un modèle
python scripts/make/model.py name=Motivation

# Générer un test
python scripts/make/test.py name=Motivation
```