
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.engine import URL

from env_loader import env

# Read database configuration from .env
DB_ENGINE = env("DB_ENGINE", "postgresql")
DB_NAME = env("DB_NAME")
DB_USERNAME = env("DB_USERNAME")
DB_PASSWORD = env("DB_PASSWORD")
DB_HOST = env("DB_HOST", "localhost")
DB_PORT = int(env("DB_PORT", "5432"))

# Create database URL
DATABASE_URL = URL.create(
    drivername="postgresql+psycopg",
    username=DB_USERNAME,
    password=DB_PASSWORD,
    host=DB_HOST,
    port=DB_PORT,
    database=DB_NAME,
)

# Create SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Create database session
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Create Base
Base = declarative_base()


# Database dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()




# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.ext.declarative import declarative_base
#
# DATABASE_URL = "postgresql+psycopg://ajmal4619:Ajmal123@localhost:5432/school_db"
# engine = create_engine(DATABASE_URL)
#
# SessionLocal = sessionmaker(
#     autocommit=False,
#     autoflush=False,
#     bind=engine
# )
#
# Base = declarative_base()
#
#
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()
