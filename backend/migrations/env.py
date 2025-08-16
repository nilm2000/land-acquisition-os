from __future__ import with_statement
from alembic import context
from sqlalchemy import engine_from_config, pool
from logging.config import fileConfig
import os

from dotenv import load_dotenv
from app.models import Base  # Adjust to your models

# Load .env variables
load_dotenv()

# Alembic Config object
config = context.config

# Logging setup
fileConfig(config.config_file_name)

# Convert async URL to sync for Alembic
DATABASE_URL = os.getenv("DATABASE_URL") or ""
if DATABASE_URL.startswith("postgresql+asyncpg"):
    DATABASE_URL = DATABASE_URL.replace("postgresql+asyncpg", "postgresql+psycopg2")

# Apply DB URL to Alembic config
config.set_main_option("sqlalchemy.url", DATABASE_URL)

# Target metadata for 'autogenerate' support
target_metadata = Base.metadata

# Ignore specific PostGIS & Tiger Geocoder tables
IGNORE_TABLES = {
    "county", "loader_lookuptables", "zip_state_loc", "featnames", "addrfeat",
    "tabblock20", "bg", "pagc_rules", "tabblock", "addr", "zip_lookup_all",
    "pagc_gaz", "cousub", "tract", "zcta5", "spatial_ref_sys", "edges", "state",
    "layer", "topology", "loader_variables", "zip_state", "place",
    "geocode_settings_default", "state_lookup", "faces", "street_type_lookup",
    "zip_lookup", "loader_platform", "county_lookup", "direction_lookup",
    "pagc_lex", "place_lookup", "geocode_settings", "secondary_unit_lookup",
    "countysub_lookup", "zip_lookup_base"
}

def include_object(object, name, type_, reflected, compare_to):
    if type_ == "table" and name in IGNORE_TABLES:
        return False
    return True

def run_migrations_offline():
    """Run migrations in 'offline' mode."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        include_object=include_object
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    """Run migrations in 'online' mode."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            include_object=include_object
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
