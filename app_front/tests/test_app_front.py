import os
from unittest.mock import patch

from streamlit.testing.v1 import AppTest

CURRENT_DIR = os.path.dirname(__file__)
ABS_PATH_APP = os.path.join(CURRENT_DIR, "../main.py")


def test_streamlit_api_connection_success():
    """Teste si l'UI affiche 'success' quand l'API répond 200."""
    at = AppTest.from_file(ABS_PATH_APP)

    # On "mock" (simule) la réponse de requests.get
    with patch("requests.get") as mock_get:
        # On définit ce que le faux bouton 'get' doit renvoyer
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"message": "Hello World"}

        at.run()

        # On simule le clic sur le bouton (le premier bouton trouvé)
        at.button[0].click().run()

        # Vérifications
        assert at.success[0].value.startswith("Connexion reussi")  #
        assert not at.error  # On vérifie qu'il n'y a pas d'erreur affichée


def test_streamlit_api_connection_error():
    """Teste si l'UI affiche une erreur quand l'API est injoignable."""
    at = AppTest.from_file(ABS_PATH_APP)

    with patch("requests.get") as mock_get:
        # On simule une erreur de connexion
        import requests

        mock_get.side_effect = requests.exceptions.ConnectionError()

        at.run()
        at.button[0].click().run()

        # On vérifie que le message d'erreur Streamlit est bien là
        assert "Impossible de se connecter" in at.error[0].value


def test_streamlit_api_http_error():
    """Teste si l'UI affiche une erreur quand l'API répond avec un code HTTP != 200."""
    at = AppTest.from_file(ABS_PATH_APP)

    with patch("requests.get") as mock_get:
        # On simule une erreur 500 (Erreur Serveur)
        mock_get.return_value.status_code = 500

        at.run()
        # On clique sur le bouton de ping
        at.button[0].click().run()

        # On vérifie que le message d'erreur contient bien le code 500
        assert len(at.error) > 0
        assert "L'API a répondu avec une erreur : 500" in at.error[0].value


def test_streamlit_api_404_error():
    """Teste le cas spécifique d'une route non trouvée (404)."""
    at = AppTest.from_file(ABS_PATH_APP)

    with patch("requests.get") as mock_get:
        mock_get.return_value.status_code = 404

        at.run()
        at.button[0].click().run()

        assert "L'API a répondu avec une erreur : 404" in at.error[0].value
