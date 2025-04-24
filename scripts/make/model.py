import sys
from pathlib import Path


def to_snake_case(name):
    return ''.join(['_' + c.lower() if c.isupper() else c for c in name]).lstrip('_')


def create_model(name):
    model_name = name.capitalize()
    schema_name = f"{model_name}Schema"
    filename = to_snake_case(name)

    model_path = Path(f"app/models/{filename}.py")
    schema_path = Path(f"app/schemas/{filename}.py")

    if model_path.exists() or schema_path.exists():
        print("❌ Le modèle ou le schéma existe déjà.")
        return

    # Modèle SQLAlchemy
    model_content = f"""from app.db import db


class {model_name}(db.Model):
    __tablename__ = '{filename}'
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
"""

    # Schéma Marshmallow
    schema_content = f"""from marshmallow import Schema, fields


class {schema_name}(Schema):
    id = fields.Int(dump_only=True)
    created_at = fields.DateTime(dump_only=True)
"""

    model_path.write_text(model_content)
    schema_path.write_text(schema_content)

    print(f"✅ Modèle créé : {model_path}")
    print(f"✅ Schéma créé : {schema_path}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python scripts/make_model.py NomModele")
    else:
        create_model(sys.argv[1])
