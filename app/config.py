import os
from pathlib import Path

from dotenv import load_dotenv

# Charge les variables depuis .env
env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)


class BaseConfig:
    SECRET_KEY = os.getenv("SECRET_KEY", "default-secret")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "default-jwt-secret")


class DevConfig(BaseConfig):
    DEBUG = True


class ProdConfig(BaseConfig):
    DEBUG = False


class TestConfig(BaseConfig):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"  # ou une base de test
