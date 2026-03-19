from unittest.mock import patch

import pandas as pd
import pytest
from models.models import Base
from modules.db_tools import (
    create_session,
    existing_citation,
    initialise_db,
    read_db,
    write_db,
)
from sqlalchemy import create_engine

# --- FIXTURES ---


@pytest.fixture(name="test_engine")
def fixture_test_engine():
    """Moteur SQLite en mémoire pour les tests réussis."""
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)
    return engine


@pytest.fixture
def mock_db_session(test_engine):
    """Mock automatique pour utiliser SQLite au lieu de Postgres."""
    with patch("modules.db_tools.create_session") as mocked:
        from sqlalchemy.orm import sessionmaker

        Session = sessionmaker(bind=test_engine)
        mocked.side_effect = lambda: Session()
        yield mocked


# --- TESTS DE SUCCÈS (Déjà vus) ---


def test_write_and_read_workflow(mock_db_session):
    df_in = pd.DataFrame({"text": ["Citation A"]})
    write_db(df_in)
    df_out = read_db()
    assert len(df_out) == 1
    assert df_out.iloc[0]["text"] == "Citation A"


def test_initialise_db(test_engine):
    """Teste la création des tables."""
    with patch("modules.db_tools.ENGINE", test_engine):
        # On vérifie que la fonction s'exécute sans erreur
        initialise_db()


# --- TESTS DES CAS D'ERREURS (Pour la couverture des 'except') ---


def test_create_session_exception():
    """Couvre le bloc 'except' de create_session (Lignes 40-42)."""
    # On passe un objet invalide au lieu d'un engine pour forcer une erreur
    invalid_engine = "not_an_engine"
    session = create_session(engine=invalid_engine)
    assert session is None


def test_existing_citation_no_session():
    """Couvre le cas où la session ne peut pas être établie (Lignes 48-49)."""
    with patch("modules.db_tools.create_session", return_value=None):
        result = existing_citation()
        assert result == {}


def test_write_db_no_session():
    """Couvre l'erreur de session dans write_db."""
    with patch("modules.db_tools.create_session", return_value=None):
        # Ne doit pas crash, juste logger l'erreur
        write_db(pd.DataFrame({"text": ["test"]}))


def test_write_db_rollback_on_error(mock_db_session):
    """Couvre le rollback en cas d'erreur d'écriture (Lignes 86-88)."""
    # On simule un DataFrame qui va causer une erreur (colonne manquante)
    df_invalid = pd.DataFrame({"wrong_column": ["data"]})

    # On vérifie que l'erreur est gérée (loguée) et n'interrompt pas le programme
    write_db(df_invalid)
    # Si le code arrive ici, c'est que le 'except' a fonctionné


def test_initialise_db_exception():
    """Couvre l'erreur de connexion dans initialise_db (Lignes 119-124)."""
    # On mock Base.metadata.create_all pour qu'il lève une erreur
    with patch(
        "models.models.Base.metadata.create_all",
        side_effect=Exception("DB Unreachable"),
    ):
        initialise_db()
        # Le logger.error est appelé, le test passe.


def test_read_db_empty_or_error():
    """Couvre les cas où read_db ne trouve rien ou échoue."""
    with patch("modules.db_tools.create_session", return_value=None):
        df = read_db()
        assert isinstance(df, pd.DataFrame)
        assert df.empty
