import os
import random
from typing import List

import pandas as pd
import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from modules.db_tools import initialise_db, read_db, write_db
from pydantic import BaseModel, Field

load_dotenv()


class QuoteRequest(BaseModel):
    # Verifie que le format soit conforme au modèle
    # text : NonEmptyString
    # text : str
    text: str = Field(min_length=1, description="donner un texte pour la citation")


class QuoteResponse(BaseModel):
    # Verifie que le format soit conforme au modèle
    id: int
    text: str


initialise_db()

API_PORT = os.getenv("FASTAPI_PORT")
API_ROOT_URL = f"http://mon_api:{API_PORT}"

app = FastAPI(title="API")


@app.get("/")
def read_root():
    return {"Hello": "World", "status": "API is running"}


@app.post("/insert/", response_model=QuoteResponse)
def insert_quote(quote: QuoteRequest):
    """
    Insert une nouvelle citation

    :param quote: Description
    :type quote: QuoteRequest
    """
    # 1. trouver de dernier id du csv
    df = read_db()
    # 2. donner un id à sa citation
    if df.empty:
        new_id = 1
    elif df.index.max() <= 0:
        new_id = 1
    else:
        # pour le cas CSV
        new_id = 1 + df.index.max()

    # 3. enregister le fichier csv
    # Verifier que le texte n'est pas vide
    # 3.1 création d'une nouvelle ligne
    objet = {"text": [quote.text]}
    new_row = pd.DataFrame(objet, index=[new_id])

    # 3.2 enregistrer le fichier csv
    df = pd.concat([df, new_row])
    write_db(df)

    # 4. envoi à l'app la citation avec id
    return {"id": new_id, "text": quote.text}


@app.get("/read/", response_model=List[QuoteResponse])
def read_all_quotes():
    df = read_db()
    return (
        df.reset_index().rename(columns={"id": "id", "text": "text"}).to_dict("records")
    )


@app.get("/read/{id}", response_model=QuoteResponse)
def read_specific_quotes(id: int):
    # il me faut toutes les citations pour les connaitres
    df = read_db()
    # filtre par l'id concerné
    if id not in df.index:
        raise HTTPException(
            status_code=404, detail=f"Citation avec ID {id} non trouvée"
        )
    quote_data = df.loc[id].to_dict()
    quote_data["id"] = id
    # retourne les résultats
    return quote_data


@app.get("/read/random/", response_model=QuoteResponse)
def read_random_quotes():
    # il me faut toutes les citations pour les connaitres
    df = read_db()
    # filtre par l'id concerné
    if df.empty:
        raise HTTPException(
            status_code=404, detail="Citation avec aléatoire non trouvée"
        )

    random_id = random.choice(df.index)
    quote_data = df.loc[random_id].to_dict()
    quote_data["id"] = random_id
    # retourne les résultats
    return quote_data


if __name__ == "__main__":
    # Récupération du port
    port_env = os.getenv("FASTAPI_PORT", "9090")
    host_url = "0.0.0.0"  # Impératif pour Docker

    try:
        port = int(port_env)
    except (ValueError, TypeError):
        port = 9090

    print(f"--- Démarrage de l'API sur le port {port} ---")

    # Lancer Uvicorn de manière bloquante
    # Assure-toi que "main" est le nom de ton fichier actuel (main.py)
    # et "app" le nom de ta variable FastAPI (app = FastAPI())
    uvicorn.run(app, host=host_url, port=port, log_level="debug")
