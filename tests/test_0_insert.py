import json
import os
from unittest.mock import patch

import requests
from streamlit.testing.v1 import AppTest

# Chemin vers votre fichier frontend
ABS_PATH_APP = os.path.join(os.path.dirname(__file__), "../pages/0_insert.py")


def test_insert_quote_success():
    """Teste l'ajout réussi d'une citation."""
    at = AppTest.from_file(ABS_PATH_APP)

    # On mocke l'appel POST
    with patch("requests.post") as mock_post:
        # Configuration de la fausse réponse API
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {
            "id": 42,
            "text": "Ma super citation",
        }

        at.run()

        # 1. On remplit le champ texte (le premier text_input trouvé)
        at.text_input[0].set_value("Ma super citation")

        # 2. On clique sur le bouton du formulaire (soumission)
        at.button[0].click().run()

        # Vérifications
        assert at.success[0].value == "Citation ajoutée ! ID: 42"
        assert json.loads(at.json[0].value) == {"id": 42, "text": "Ma super citation"}
        # Optionnel : vérifier que l'API a été appelée avec les bons arguments
        mock_post.assert_called_once()


def test_insert_quote_api_error():
    """Teste l'affichage d'une erreur si l'API renvoie un code != 200."""
    at = AppTest.from_file(ABS_PATH_APP)

    with patch("requests.post") as mock_post:
        mock_post.return_value.status_code = 400

        at.run()
        at.text_input[0].set_value("Erreur test")
        at.button[0].click().run()

        assert "L'API a répondu avec une erreur : 400" in at.error[0].value


def test_insert_quote_connection_error():
    """Teste l'affichage de l'alerte quand l'API est hors ligne (ConnectionError)."""
    at = AppTest.from_file(ABS_PATH_APP)

    with patch("requests.post") as mock_post:
        # On simule une erreur de connexion (le serveur ne répond pas du tout)
        mock_post.side_effect = requests.exceptions.ConnectionError()

        at.run()

        # On remplit le champ et on valide le formulaire
        at.text_input[0].set_value("Test connexion")
        at.button[0].click().run()

        # 1. Vérification du message d'erreur rouge (st.error)
        assert len(at.error) > 0
        assert "Impossible de se connecter à l'API" in at.error[0].value

        # 2. Vérification du message d'avertissement jaune (st.warning)
        assert len(at.warning) > 0
        assert (
            "Veuillez vous assurer que le serveur est bien lancé" in at.warning[0].value
        )
