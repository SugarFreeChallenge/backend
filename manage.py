from flask.cli import FlaskGroup
from app import create_app
from app.db import db
from flask_migrate import Migrate
import os

app = create_app()
cli = FlaskGroup(app)

# Initialise Flask-Migrate
migrate = Migrate(app, db)

# Optionnel : créer une commande personnalisée
@cli.command("create-db")
def create_db():
    """Crée les tables dans la base."""
    db.create_all()
    print("Base de données créée.")

@cli.command("drop-db")
def drop_db():
    """Supprime toutes les tables (⚠️)."""
    db.drop_all()
    print("Base de données supprimée.")

if __name__ == "__main__":
    cli()
