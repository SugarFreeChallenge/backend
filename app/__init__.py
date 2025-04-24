from flask import Flask
from app.db import db
from app.routes import register_routes
from app.config import DevConfig, ProdConfig, TestConfig
import os


def create_app():
    app = Flask(__name__)

    # Choix de la config selon ENV
    env = os.getenv("FLASK_ENV", "development")

    if env == "production":
        app.config.from_object(ProdConfig)
    elif env == "testing":
        app.config.from_object(TestConfig)
    else:
        app.config.from_object(DevConfig)

    db.init_app(app)
    register_routes(app)

    return app
