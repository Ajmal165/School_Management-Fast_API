from logging.config import fileConfig

from sqlalchemy import create_engine, pool
from alembic import context

# Import database configuration
from database import Base, DATABASE_URL

# Import all models so Alembic can detect tables
from src.competition import model as competition_model
from src.entry import model as entry_model
from src.user import model as user_model


# Alembic Config object
config = context.config


# Configure logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)


# SQLAlchemy model metadata
target_metadata = Base.metadata


# --------------------------------------------------
# OFFLINE MIGRATION
# --------------------------------------------------

def run_migrations_offline() -> None:
    """
    Run migrations in offline mode.

    This mode generates SQL migration scripts
    without establishing a database connection.
    """

    context.configure(
        url=DATABASE_URL.render_as_string(hide_password=False),
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        compare_type=True,
    )

    with context.begin_transaction():
        context.run_migrations()


# --------------------------------------------------
# ONLINE MIGRATION
# --------------------------------------------------

def run_migrations_online() -> None:
    """
    Run migrations in online mode.

    This mode establishes a database connection
    and executes migrations against PostgreSQL.
    """

    connectable = create_engine(
        DATABASE_URL,
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:

        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,
        )

        with context.begin_transaction():
            context.run_migrations()

    connectable.dispose()


# --------------------------------------------------
# EXECUTE MIGRATIONS
# --------------------------------------------------

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
