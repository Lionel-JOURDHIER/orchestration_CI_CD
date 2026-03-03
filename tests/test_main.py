import subprocess
import sys
from pathlib import Path

# On force l'ajout de la racine du projet au chemin de recherche
# pour être sûr que 'import main' fonctionne peu importe où on lance le test
sys.path.insert(0, str(Path(__file__).parent.parent))

from app.main import main


def test_main_output(capsys):
    """Vérifie que la fonction main affiche le message attendu."""
    main()

    # Capture la sortie du terminal
    captured = capsys.readouterr()

    # .strip() permet d'ignorer les espaces ou sauts de ligne inutiles
    assert captured.out.strip() == "Hello from mlobs2!"


def test_script_execution():
    """Teste l'exécution du fichier main.py en tant que script (CLI)."""
    # On trouve la racine du projet (le dossier qui contient 'tests')
    # .resolve() transforme le chemin en chemin absolu sans '..'
    root_dir = Path(__file__).parent.parent.resolve()
    script_path = root_dir / "app" / "main.py"

    # On lance le fichier
    result = subprocess.run(
        [sys.executable, str(script_path)], capture_output=True, text=True
    )
    # On vérifie le résultat
    assert result.returncode == 0
    assert "Hello from mlobs2!" in result.stdout
