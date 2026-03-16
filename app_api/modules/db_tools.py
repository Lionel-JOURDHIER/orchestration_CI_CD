import os

import pandas as pd
from loguru import logger
from models.models import Citations
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# On récupère les variables d'environnement (définies dans ton docker-compose)
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_DB = os.getenv("POSTGRES_DB")
# Note : "database" est le nom du service dans ton docker-compose
SQLALCHEMY_DATABASE_URL = (
    f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@database:5432/{POSTGRES_DB}"
)

ENGINE = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=ENGINE)
Base = declarative_base()


def create_session(engine=ENGINE):
    """
    Create and return a new SQLAlchemy session.

    Args :
        engine : sqlalchemy.Engine
            The SQLAlchemy engine connected to the database.

    Returns :
        Session
            A new SQLAlchemy session instance.
    """
    try:
        # create the tables
        Base.metadata.create_all(engine)
        # open the session
        Session = sessionmaker(bind=engine)
        return Session()
    except Exception as e:
        logger.error(f"Erreur lors de la création de la session : {e}")
        return None


def existing_citation():
    session = create_session()
    try:
        existing_citations = {p.text: p.id for p in session.query(Citations).all()}
        return existing_citations
    finally:
        session.close()


def write_db(df: pd.DataFrame):
    """
    Write a SQLLite file from a pandas DataFrame

    Args :
        df: DataFrame with data you want to write in a file

    Returns :
        None
    """
    session = create_session()
    if not session:
        return

    try:
        session = create_session()
        citations_to_add = []
        existing_citations = existing_citation()
        for _, row in df.iterrows():
            text = str(row["text"])
            if text not in existing_citations:
                citation = Citations(text=text)
                citations_to_add.append(citation)

        if citations_to_add:
            session.add_all(citations_to_add)

            session.commit()
            logger.info(f"{len(citations_to_add)} citations ajoutées.")
    except Exception as e:
        session.rollback()
        logger.error(f"Erreur d'écriture : {e}")
    finally:
        session.close()


def read_db():
    """
    Read a SQLLite file from the path DB_FILE_PATH

    :returns: DataFrame with data you read from the file
    :type df: pd.DataFrame
    """
    session = create_session()
    if not session:
        return pd.DataFrame()
    try:
        query = session.query(Citations).all()
        db = [{"id": p.id, "text": p.text} for p in query]
        df = pd.DataFrame(db)
        if not df.empty:
            df = df.set_index("id")
            df = check_df(df)
        return df
    finally:
        session.close()


def initialise_db():
    """
    Write an empty SQLLite file with 2 columns 'id' and 'text'
    """
    try:
        # On tente de créer les tables (Metadata)
        Base.metadata.create_all(ENGINE)
        logger.info("Base de données PostgreSQL initialisée (Tables vérifiées).")
    except Exception as e:
        logger.error(f"Impossible de joindre PostgreSQL : {e}")


def check_df(df: pd.DataFrame):
    """
    Read a dataframe
    :type df: pd.DataFrame
    :returns: DataFrame with empty rows filled with 'NULL'
    """
    for index, row in df.iterrows():
        for col in df.columns:
            if pd.isna(row[col]):
                logger.info(
                    f"NaN trouvé à la ligne {index}, colonne '{col}' remplacé par la valeur 'NULL'"
                )
    df = df.fillna("NULL")
    write_db(df)
    return df
