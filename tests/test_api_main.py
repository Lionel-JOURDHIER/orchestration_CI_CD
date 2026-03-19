import multiprocessing
import time

import pytest
import requests
import uvicorn
from main import app

# --- CONFIGURATION DU SERVEUR AUTOMATIQUE ---


def run_server():
    """Fonction pour lancer Uvicorn dans un processus séparé."""
    uvicorn.run(app, host="127.0.0.1", port=8005, log_level="error")


@pytest.fixture(scope="module", autouse=True)
def setup_server():
    """Lance le serveur avant les tests et le coupe après."""
    proc = multiprocessing.Process(target=run_server, daemon=True)
    proc.start()
    time.sleep(1.5)  # Temps de chauffe pour que le port 8005 s'ouvre
    yield
    proc.terminate()


# --- TESTS AVEC REQUESTS ---

BASE_URL = "http://127.0.0.1:8005"


def test_read_root_requests():
    """Teste la racine '/' avec requests."""
    response = requests.get(f"{BASE_URL}/")
    assert response.status_code == 200


def test_get_citations_requests():
    """Teste la route de lecture."""
    # Note : Le mock ici ne fonctionnera que si le serveur tourne
    # dans le MÊME processus. Pour du pur requests sur un serveur distant,
    # on teste la VRAIE base de données (Intégration).
    response = requests.get(f"{BASE_URL}/read")  # Adapte à ta route
    assert response.status_code == 200
    assert isinstance(response.json(), (list, dict))


def test_post_citation_requests():
    """Teste l'ajout d'une citation via requests."""
    # 1. Vérifie bien que l'URL correspond à ton @app.post dans main.py
    # Si ton main.py dit @app.post("/create"), mets "/create" ici.
    URL_CIBLE = f"{BASE_URL}/insert"

    payload = {"text": "Test via requests", "author": "Robot"}

    response = requests.post(URL_CIBLE, json=payload)

    # 2. Debug : si ça rate encore, décommente la ligne suivante pour voir l'erreur
    # print(response.json())

    assert response.status_code in [200, 201]
