import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

load_dotenv()

# Récupération des variables (les mêmes que dans ton .env / docker-compose)
user = os.getenv("POSTGRES_USER")
password = os.getenv("POSTGRES_PASSWORD")
db_name = os.getenv("POSTGRES_DB")
host = "postgres_container"
port = os.getenv("POSTGRES_PORT", "5432")

DATABASE_URL = f"postgresql://{user}:{password}@{host}:{port}/{db_name}"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
