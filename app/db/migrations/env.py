import logging
from datetime import datetime
from logging.config import fileConfig

from alembic import context
from alembic.script import ScriptDirectory  # ✅ pour custom filename
from flask import current_app

# --- Logging standard ---
config = context.config
fileConfig(config.config_file_name)
logger = logging.getLogger("alembic.env")


# --- Format custom pour le nom des fichiers de migration ---
def slugify(message):
    return message.lower().replace(" ", "_").replace("-", "_")


def custom_revision_filename(revision, context):
    message = context.get_x_argument(as_dictionary=True).get("message", "migration")
    timestamp = datetime.now().strftime("%Y%m%d%H%M")
    return f"{timestamp}-{slugify(message)}.py"


# ⬇️ Injection du comportement custom
ScriptDirectory._rev_file = custom_revision_filename


# --- Gestion moteur SQLAlchemy ---
def get_engine():
    try:
        return current_app.extensions["migrate"].db.get_engine()
    except TypeError:
        return current_app.extensions["migrate"].db.engine


def get_engine_url():
    try:
        return get_engine().url.render_as_string(hide_password=False).replace("%", "%%")
    except AttributeError:
        return str(get_engine().url).replace("%", "%%")


config.set_main_option("sqlalchemy.url", get_engine_url())
target_db = current_app.extensions["migrate"].db


# --- Cible des métadonnées ---
def get_metadata():
    if hasattr(target_db, "metadatas"):
        return target_db.metadatas[None]
    return target_db.metadata


# --- Mode offline ---
def run_migrations_offline():
    url = config.get_main_option("sqlalchemy.url")
    context.configure(url=url, target_metadata=get_metadata(), literal_binds=True)

    with context.begin_transaction():
        context.run_migrations()


# --- Mode online ---
def run_migrations_online():
    def process_revision_directives(context, revision, directives):
        if getattr(config.cmd_opts, "autogenerate", False):
            script = directives[0]
            if script.upgrade_ops.is_empty():
                directives[:] = []
                logger.info("No changes in schema detected.")

    connectable = get_engine()

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=get_metadata(),
            process_revision_directives=process_revision_directives,
            **current_app.extensions["migrate"].configure_args,
        )

        with context.begin_transaction():
            context.run_migrations()


# --- Exécution ---
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
