# frontend/pages/0_insérer.py
import os

import pandas as pd
import requests
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

API_PORT = int(os.getenv("FASTAPI_PORT", "8000"))
API_ROOT_URL = f"http://0.0.0.0:{API_PORT}"
API_URL = API_ROOT_URL + "/read/"

st.title("Lire toutes les citations")

if st.button("Charger les données"):
    st.info("lire depuis l'API")

    try:
        response = requests.get(API_URL)

        if response.status_code == 200:
            result = response.json()

            df = pd.DataFrame(result)
            st.dataframe(df, width="stretch")

            st.success("Lecture de toutes les citations")
            st.balloons()
        else:
            st.error(f"Erreur de l'API avec le code {response.status_code}")
            st.write(response)

    except requests.exceptions.ConnectionError:
        st.error(f"ERREUR : Impossible de se connecter à l'API à {API_URL}")
        st.warning(
            "Veuillez vous assurer que le serveur Uvicorn est bien lancé en arrière-plan."
        )
