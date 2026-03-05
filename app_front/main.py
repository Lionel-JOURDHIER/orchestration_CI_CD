# frontend/app.py
import os

import requests
import streamlit as st
from dotenv import load_dotenv

load_dotenv()
API_PORT = int(os.getenv("FASTAPI_PORT"))
API_URL = f"http://0.0.0.0:{API_PORT}/"

# pour des raisons de sécuritées.
# il faut stocker cela comme variable d'environnement.


st.title("Démonstration d'API avec FastAPI et Streamlit")

st.subheader("verification de l'API")

# --- LE BOUTON ---
if st.button("ping l'API (Route /)"):
    try:
        # 1. --- Requetes GET  vers route principale ---
        reponse = requests.get(API_URL)
        if reponse.status_code == 200:
            # 2. --- Si il y a un resultat l'afficher ---
            st.success(f"Connexion reussi à l'API FastAPI sur http://{API_URL} ! ")
            st.code(f"Statuts HTTP : {reponse.status_code}")
            st.json(reponse.json())
        else:
            st.error(f"L'API a répondu avec une erreur : {reponse.status_code}")

    except requests.exceptions.ConnectionError:
        st.error(f"ERREUR : Impossible de se connecter à l'API à {API_URL}")
        st.warning(
            "Veuillez vous assurer que le serveur est bien lancé en arrière plans"
        )
