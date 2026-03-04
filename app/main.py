import pandas as pd

from app.modules.mon_module import add, print_data, square, sub


def get_values_from_csv(filepath: str) -> pd.DataFrame:
    """Extrait une colonne spécifique d'un CSV sous forme de liste de nombres.

    Args :
       filepath (str): Le chemin vers le fichier CSV.

    Returns:
       pd.DataFrame: Un DataFrame contenant les données extraites du CSV.
    """
    return pd.read_csv(filepath)


if __name__ == "__main__":  # pragma: no cover
    filepath = "app/moncsv.csv"
    df = get_values_from_csv(filepath)
    print_data(df)  # Affiche le DataFrame dans le terminal
    print(add(3, 5))  # Addition
    print(sub(10, 4))  # Soustraction
    print(square(9))  # Racine
