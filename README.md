# Architecture de base ToolBox

[![Documentation](https://img.shields.io/badge/Documentation-GitHub%20Pages-blue?logo=github&logoColor=white)](https://Lionel-JOURDHIER.github.io/Toolbox_MLObs/) [![Code](https://img.shields.io/badge/Code-0.1.0-181717?logo=github)](https://github.com/Lionel-JOURDHIER/Toolbox_MLObs) ![Deploy Documentation](https://github.com/Lionel-JOURDHIER/Toolbox_MLObs/actions/workflows/documentation.yml/badge.svg) [![Python Tests](https://github.com/Lionel-JOURDHIER/Toolbox_MLObs/actions/workflows/test.yml/badge.svg)](https://github.com/Lionel-JOURDHIER/Toolbox_MLObs/actions)  [![Ruff Status](https://github.com/Lionel-JOURDHIER/Toolbox_MLObs/actions/workflows/ruff.yml/badge.svg)](https://github.com/Lionel-JOURDHIER/Toolbox_MLObs/actions) ![Ruff](https://img.shields.io/badge/Ruff-checked-green?logo=ruff&logoColor=white)
![Python](https://img.shields.io/badge/python-3.11-blue.svg)  ![Linter](https://img.shields.io/badge/linter-ruff-orange.svg)  ![License](https://img.shields.io/badge/license-MIT-green.svg) ![uv](https://img.shields.io/badge/managed%20by-uv-de5b41.svg) ![Docker](https://img.shields.io/badge/docker-ready-blue.svg?logo=docker) ![Last Commit](https://img.shields.io/github/last-commit/Lionel-JOURDHIER/Toolbox_MLObs) ![Repo Size](https://img.shields.io/github/repo-size/Lionel-JOURDHIER/Toolbox_MLObs) ![Open Issues](https://img.shields.io/github/issues/Lionel-JOURDHIER/Toolbox_MLObs)


> Version actuelle : `v0.1.0`

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

### 2.1 Installation dans uv
Pour installer RUFF dans votre projet, utilisez la commande suivante :
```bash
uv add --dev ruff
```


### 2.2 Configuration (`pyproject.toml`)

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

### 2.5 Commandes de maintenance

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

### 3.5. Compilation
Utilise l'environnement virtuel géré par `uv` pour lancer Sphinx qui compile la documentation. Le format de sortie est HTML(Site Web)
```bash
# Depuis la racine du projet
uv run sphinx-build -b html docs/source public
```

Vérifier la documentation HTML : `uv run python -m webbrowser public/index.html`

## 4. Installation Pytest
Pytest est le framework de référence pour valider la logique de calcul. Couplé à pytest-cov, il permet de mesurer la couverture de code (pourcentage de lignes testées).

### 4.1 Installation des dépendances
Ajouter le dépendences pytest et pytest-cov à votre environnement de développement : 

```bash
uv add --dev pytest pytest-cov
```

### 4.2 Configuration (pytest.ini ou pyproject.toml)
Pour automatiser les options (comme la couverture de code) sans les retaper, créez un fichier pytest.ini à la racine :
```Ini, TOML[pytest]
testpaths = tests
python_files = test_*.py
# addopts : lance automatiquement le coverage sur le dossier app/
addopts = -v --cov=app --cov-report=term-missing --cov-report=html
```

### 4.3 Commandes de test
| Action | Commande | Résultat |
| :--- | :--- | :--- |
| **Lancer les tests** | `uv run pytest` | Affiche les succès/échecs et le rapport de couverture. |
| **Rapport HTML** | `uv run python -m webbrowser htmlcov/index.html` | Ouvre une vue détaillée des lignes non testées. |

## 5. Mise en place des GitHub Actions

Les **GitHub Actions** automatisent votre flux de travail. À chaque fois que vous envoyez du code (`git push`), un serveur distant exécute vos tests, vérifie votre style de code et met à jour votre documentation.

### 5.1. Pourquoi utiliser une CI/CD ?

* **Garde-fou :** Empêche l'intégration de code qui casse les calculs existants.
* **Consistance :** Garantit que le code est formaté de la même manière pour tous les collaborateurs.
* **Automatisation :** Plus besoin de compiler la documentation manuellement, elle est toujours à jour.

### 5.2. Configuration du Workflow (`.github/workflows/main.yml`)

Créez un fichier YAML à cet emplacement exact dans votre projet. Ce fichier ordonne à GitHub d'utiliser `uv` pour orchestrer les tâches.

```yaml
name: Python Quality & Doc
on:
  push:
    branches: [ main, dev ]
  pull_request:
    branches: [ main ]

permissions:
  contents: write
  pages: write
  id-token: write

jobs:
  build-and-test:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Install uv
        uses: astral-sh/setup-uv@v5
        with:
          enable-cache: true

      - name: Install dependencies
        run: uv sync --all-extras

      - name: Linter (Ruff)
        run: |
          uv run ruff check .
          uv run ruff format --check .

      - name: Tests (Pytest)
        run: uv run pytest

      - name: Build Documentation (Sphinx)
        run: |
          uv run sphinx-apidoc -f -o docs/source ./app
          uv run sphinx-build -b html docs/source public

      - name: Upload Artifact
        uses: actions/upload-pages-artifact@v3
        with:
          path: 'public'

  deploy:
    needs: build-and-test
    if: github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    steps:
      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v4
```

### 5.3 Activation sur Github 

Pour que le déploiement fonctionne, vous devez autoriser GitHub Actions à publier des pages :

Clique sur l'onglet Settings (en haut à droite).

Dans le menu de gauche, clique sur Pages.

Sous la section Build and deployment > Source, change "Deploy from a branch" pour "GitHub Actions".

Votre documentation sera alors accessible à l'adresse : https://<votre-pseudo>.github.io/<nom-du-repo>/

