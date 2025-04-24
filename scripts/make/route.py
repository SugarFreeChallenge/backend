import sys
from pathlib import Path


def create_route(name):
    path = Path(f"app/routes/{name}.py")
    if path.exists():
        print(f"❌ Le fichier {path} existe déjà.")
        return

    content = f'''from flask import Blueprint, jsonify

{name}_bp = Blueprint("{name}", __name__)


@{name}_bp.route("/", methods=["GET"])
def index():
    return jsonify({{"message": "Hello from {name}!"}})
'''

    path.write_text(content)
    print(f"✅ Route {name} créée dans {path}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python scripts/make_route.py <nom_de_la_route>")
    else:
        create_route(sys.argv[1])
