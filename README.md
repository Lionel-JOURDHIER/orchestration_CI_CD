# Toobox projet

Ce projet utilise une suite d'outils modernes pour garantir la qualité du code, la robustesse des calculs et la clarté de la documentation technique.

---
## 1. Structure du Template de Code

Un projet doit être organisé de manière hermétique pour garantir la collaboration et la maintenance :

```
.
├── app/                   # Code source de l'application
├── tests/                 # Tests unitaires et d'intégration (Pytest)
├── docs/                  # Documentation technique (Sphinx/Furo)
├── pyproject.toml         # Configuration centralisée des outils
├── uv.lock                # Verrouillage des dépendances (généré par uv)
├── Dockerfile             # Conteneurisation de l'application
└── README.md              # Vitrine du projet (Badges, Infos, Guide)

```

Utilisez `uv init` pour initialiser le projet et `uv add x` pour ajouter les bibliothèques.
`uv run x` (application ou test) pour executer en local.

---

## 2. Qualité du Code avec Ruff

**Ruff** est notre linter et formateur de code ultra-rapide (écrit en Rust). Il remplace à lui seul Black, Isort et Flake8.

**Rôle :** Garantir une base de code homogène, lisible et détecter les erreurs potentielles (variables inutilisées, imports mal classés, etc.) avant l'exécution.

### Installation dans uv
Pour installer RUFF dans votre projet, utilisez la commande suivante :
```bash
uv add --dev ruff
```


### 2.1 Configuration (`pyproject.toml`)

Pour confirurer que RUFF est uttilisé sur le projet, ajoutez la section suivante dans votre `pyproject.toml` :

```toml
[tool.ruff]
line-length = 88
target-version = "py311"

[tool.ruff.lint]
select = ["E", "W", "F", "I", "D"] # Erreurs, Warnings, Pyflakes, Isort, Docstrings
ignore = ["D100"] # On autorise l'absence de docstring en tout début de fichier
```

### 2.3 Analyse de la configuration Ruff (`pyproject.toml`)

| Code | Catégorie | Ce que Ruff vérifie |
| :--- | :--- | :--- |
| **E** | **Errors (PEP8)** | Les erreurs de style (espaces, retours à la ligne, indentation). |
| **W** | **Warnings (PEP8)** | Les avertissements de style moins critiques. |
| **F** | **Pyflakes** | Les erreurs logiques (variables non définies, imports inutilisés). |
| **I** | **Isort** | Le tri alphabétique et le regroupement automatique des `import`. |
| **D** | **Pydocstyle** | La présence et la qualité des docstrings (conventions PEP 257). |

---

### 2.4 Exceptions configurées ou possibles : (`ignore`)

| Code | Règle ignorée | Raison habituelle |
| :--- | :--- | :--- |
| **D100** | Missing docstring in public module | Évite d'avoir à écrire un résumé obligatoire tout en haut de chaque fichier `.py`. |
| **D101** | Missing docstring in public class | Évite d'avoir à écrire une docstring pour chaque classe, surtout si elles sont auto-explicatives. |
| **D102** | Missing docstring in public method | Évite d'avoir à écrire une docstring pour chaque méthode, surtout si elles sont simples. |
| **D103** | Missing docstring in public function | Évite d'avoir à écrire une docstring pour chaque fonction, surtout si elles sont courtes. |
| **D104** | Missing docstring in public package | Évite d'avoir à écrire une docstring pour les packages (dossiers avec `__init__.py`). |
| **D200** | One-line docstring should fit on one line with quotes | Permet les docstrings multi-lignes même pour les fonctions très courtes. |
| **D400** | First line should end with a period | Permet de ne pas mettre un point à la fin de la première ligne d'une docstring. |
| **D401** | First line should be in imperative mood | Permet de ne pas formuler la première ligne d'une docstring comme une commande (ex: "Calculate" au lieu de "Calculates"). |

### Commandes de maintenance

| Action | Commande |
| :--- | :--- |
| **Vérifier** | `uv run ruff check .` |
| **Réparer** | `uv run ruff check . --fix` |
| **Formater** | `uv run ruff format .` |

---

## 3. Installation de Sphynx-Furo
### 3.1. Installation des dépendances

```powershell
uv add --dev furo myst_parser sphinxcontrib-bibtex

```

### 3.2. Initialisation

```powershell
mkdir docs
cd docs
uv run sphinx-quickstart
# Répondre aux questions (Projet, Nom, Version)
cd ..

```

### 3.3. Configuration (`docs/source/conf.py`)

```python
import os
import sys
sys.path.insert(0, os.path.abspath('../../'))

extensions = [
    'sphinx.ext.autodoc',       # INDISPENSABLE : extrait la doc des docstrings
    'sphinx.ext.napoleon',      # Supporte le format Google/NumPy (plus lisible)
    'sphinx.ext.viewcode',      # Ajoute un lien [source] à côté de tes fonctions
    'sphinx.ext.mathjax',       # Pour le rendu des formules LaTeX
    'myst_parser',              # Pour lire les fichiers .md (README, etc.)
    'sphinxcontrib.bibtex',     # Pour la gestion du fichier .bib
]

html_theme = "furo"
bibtex_bibfiles = ['refs.bib']

html_theme_options = {
    "light_css_variables": {
        "color-brand-primary": "#7C4DFF",
        "color-brand-content": "#7C4DFF",
    },
}

```


### 3.4 Générer automatiquement les rst
Si vous voulez mettre à jour votre documentation en écrasant les anciens fichiers et en séparant bien chaque module sur sa propre page, utilisez ceci depuis la racine du projet :

```bash
# Depuis la racine du projet
sphinx-apidoc -f -e -o docs/source/ ./app

```
#### Les options pour la génération automatique

Voici les options les plus utiles pour personnaliser votre génération :

| Option | Description | Utilité |
| :--- | :--- | :--- |
| **`-o`** / **`--output-dir`** | Chemin du répertoire de destination. | Indispensable pour séparer les fichiers `.rst` de votre code source. |
| **`-f`** / **`--force`** | Force l'écrasement des fichiers existants. | À utiliser si vous avez renommé des fonctions ou des fichiers `.py`. |
| **`-n`** / **`--dry-run`** | Simule la génération sans créer de fichiers. | Pratique pour tester la commande sans risquer d'écraser vos fichiers. |
| **`-M`** | Met les modules avant les sous-packages. | Change l'ordre d'affichage dans la table des matières. | **`-e`** / **`--separate`** | Met chaque module sur sa propre page. | Rend la navigation plus fluide dans la documentation finale. |

### 3.4. Compilation
Utilise l'environnement virtuel géré par `uv` pour lancer Sphinx qui compile la documentation. Le format de sortie est HTML(Site Web)
```bash
# Depuis la racine du projet
uv run sphinx-build -b html docs/source public
```

Vérifier la documentation HTML : `uv run python -m webbrowser public/index.html`


