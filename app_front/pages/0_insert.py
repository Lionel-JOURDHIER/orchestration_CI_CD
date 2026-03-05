import os

import requests
import streamlit as st
from dotenv import load_dotenv

load_dotenv()
API_PORT = int(os.getenv("FASTAPI_PORT"))
API_ROOT_URL = f"http://0.0.0.0:{API_PORT}"
API_URL = API_ROOT_URL + "/insert/"


# Configuration de la page
st.set_page_config(page_title="Mur de Projets", layout="wide")

#! mettre en place la connexion user si on a le temps.
# if st.session_state.user is None:
#     tab1, tab2 = st.tabs(["Connexion", "Création de compte"])

#     with tab2:
#         with st.form("signup"):
#             new_email = st.text_input("Email")
#             new_password = st.text_input("Mot de passe", type="password")
#             if st.form_submit_button("S'inscrire"):
#                 data = {"email": new_email, "password": new_password}
#                 try:
#                     requests.post("/signup", json=data)
#                     st.success("Compte créé !")
#                 except Exception as e:
#                     st.error(f"Erreur : {e}")

#     with tab1:
#         with st.form("login"):
#             email = st.text_input("Email")
#             password = st.text_input("Mot de passe", type="password")
#             if st.form_submit_button("Se connecter"):
#                 data = {"email": email, "password": password}
#                 try:
#                     response = requests.post("/login", json=data)
#                     st.session_state.user = response.user
#                     st.rerun()
#                 except Exception:
#                     st.error("Identifiants incorrects")
# else:
#     st.sidebar.write(f"Connecté en tant que : {st.session_state.user}")
#     if st.sidebar.button("Déconnexion"):
#         requests.get("/logout")
#         st.session_state.user = None
#         st.rerun()
#     st.title("Inserer une nouvelle citation")

with st.form("insert form"):
    new_quote_text = st.text_input("Texte de la citation :")
    submitted = st.form_submit_button("Ajouter la citation")
    if submitted:
        data = {"text": new_quote_text}
        st.info("envoi à l'API")

        try:
            # 1. --- Requetes GET  vers route principale ---
            reponse = requests.post(API_URL, json=data)
            if reponse.status_code == 200:
                # 2. --- Si il y a un resultat l'afficher ---
                result = reponse.json()
                st.success(f"Citation ajoutée ! ID: {result['id']} ")
                st.json(result)
                st.balloons()
            else:
                st.error(f"L'API a répondu avec une erreur : {reponse.status_code}")

        except requests.exceptions.ConnectionError:
            st.error(f"ERREUR : Impossible de se connecter à l'API à {API_URL}")
            st.warning(
                "Veuillez vous assurer que le serveur est bien lancé en arrière plans"
            )
