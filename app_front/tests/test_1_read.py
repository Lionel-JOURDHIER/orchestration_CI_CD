import os
from unittest.mock import patch

import pandas as pd
from streamlit.testing.v1 import AppTest

# On pointe vers le fichier dans le dossier pages
current_dir = os.path.dirname(__file__)
ABS_PATH_READ = os.path.join(current_dir, "../pages/1_read.py")


def test_read_quotes_success():
    """Teste l'affichage réussi des données dans un DataFrame."""
    at = AppTest.from_file(ABS_PATH_READ)

    with patch("requests.get") as mock_get:
        # Données simulées renvoyées par l'API
        mock_data = [{"id": 1, "text": "Citation 1"}, {"id": 2, "text": "Citation 2"}]
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_data

        at.run()

        # On clique sur "Charger les données"
        at.button[0].click().run()

        # 1. Vérifie que le DataFrame est affiché
        assert len(at.get("dataframe")) > 0

        # 2. Vérifie le contenu (Streamlit AppTest expose le DF via .value)
        displayed_df = at.get("dataframe")[0].value
        assert isinstance(displayed_df, pd.DataFrame)
        assert len(displayed_df) == 2
        assert displayed_df.iloc[0]["text"] == "Citation 1"

        # 3. Vérifie le feedback visuel
        assert "Lecture de toutes les citations" in at.success[0].value


def test_read_quotes_api_error():
    """Teste l'affichage de l'erreur HTTP (ex: 404)."""
    at = AppTest.from_file(ABS_PATH_READ)

    with patch("requests.get") as mock_get:
        mock_get.return_value.status_code = 404

        at.run()
        at.button[0].click().run()

        assert "Erreur de l'API avec le code 404" in at.error[0].value


def test_read_quotes_connection_error():
    """Teste la panne réseau sur la page de lecture."""
    at = AppTest.from_file(ABS_PATH_READ)

    with patch("requests.get") as mock_get:
        import requests

        mock_get.side_effect = requests.exceptions.ConnectionError()

        at.run()
        at.button[0].click().run()

        assert "Impossible de se connecter à l'API" in at.error[0].value
        assert (
            "Veuillez vous assurer que le serveur Uvicorn est bien lancé"
            in at.warning[0].value
        )
