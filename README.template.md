# Architecture de base ToolBox

Ce projet %REPO% est en version %VERSION% et appartient à %USER%.

[![Code](https://img.shields.io/badge/Code-%VERSION%-181717?logo=github)](https://github.com/%USER%/%REPO%) [![Python Tests](https://github.com/%USER%/%REPO%/actions/workflows/test.yml/badge.svg)](https://github.com/%USER%/%REPO%/actions)  [![Ruff Status](https://github.com/%USER%/%REPO%/actions/workflows/ruff.yml/badge.svg)](https://github.com/%USER%/%REPO%/actions) ![Security Audit](https://img.shields.io/badge/Security-Audit_Passed-green?logo=github-actions&logoColor=white) ![Ruff](https://img.shields.io/badge/Ruff-checked-green?logo=ruff&logoColor=white)
![Python](https://img.shields.io/badge/python-3.11-blue.svg)  ![Linter](https://img.shields.io/badge/linter-ruff-orange.svg)  ![License](https://img.shields.io/badge/license-MIT-green.svg) ![uv](https://img.shields.io/badge/managed%20by-uv-de5b41.svg) ![Docker](https://img.shields.io/badge/docker-ready-blue.svg?logo=docker) ![Last Commit](https://img.shields.io/github/last-commit/%USER%/%REPO%) ![Repo Size](https://img.shields.io/github/repo-size/%USER%/%REPO%) ![Open Issues](https://img.shields.io/github/issues/%USER%/%REPO%)
![Contributeurs](https://img.shields.io/github/contributors/%USER%/%REPO%?logo=github&color=orange)

### Liste des contributeurs
[![Contributeurs](https://contrib.rocks/image?repo=%USER%/%REPO%)](https://github.com/%USER%/%REPO%/graphs/contributors)

---
## Quickstart : Toolbox MLObs

Ce guide vous permet d'installer, de tester et d'exécuter le projet immédiatement.

### 1. Installation rapide

L'utilisation de `uv` est recommandée pour une installation ultra-rapide des dépendances.

```bash
# Cloner et entrer dans le projet
git clone [https://github.com/%USER%/%REPO%.git](https://github.com/%USER%/%REPO%.git) && cd %REPO%

# Créer l'environnement virtuel et installer les dépendances d'un coup
uv venv
source .venv/bin/activate  # Sur Windows: .venv\Scripts\activate

# Installer les packages nécessaires
uv sync
```

### 2. Execution du programme

Pour exécuter le programme tout en garantissant la résolution des imports :

```bash
# Via l'environnement activé
python -m app.main

# OU directement avec uv (sans activation préalable)
uv run python -m app.main
```

### 3. Test & Qualité
```bash
# Lancer les tests avec uv
uv run pytest --cov=app --cov-report=term-missing

# Analyser le code avec ruff via uv
uv run ruff check .
```

### 4. Documentation :

La documentation technique est générée avec **Sphinx** et le thème **Furo**. Elle inclut la description des fonctions, les signatures de type et les formules mathématiques.
Veuillez suivre le protocole de documentation ici : **[3. Installation de Sphynx-Furo](#3-installation-de-sphynx-furo)** pour obtenir plus d'informations

---

## Sommaire Rapide

Pour naviguer directement vers une section spécifique du projet :

* **[2. Qualité du Code avec Ruff](#2-qualité-du-code-avec-ruff)** : Maintenir un code propre et performant.
* **[3. Installation de Sphynx-Furo](#3-installation-de-sphynx-furo)** : Générer la documentation technique.
* **[4. Installation Pytest](#4-installation-pytest)** : Configurer l'environnement de test et le coverage.
* **[5. Mise en place des GitHub Actions](#5-mise-en-place-des-github-actions)** : Automatiser les tests et le déploiement.

---

## Automatisation du README

Ce projet utilise un système de **README dynamique**. Ne modifiez pas directement le fichier `README.md`.

### Comment ça marche ?
1. Le fichier source est `README.template.md`.
2. À chaque `git push`, une **GitHub Action** :
   - Extrait la version depuis `pyproject.toml`.
   - Remplace les marqueurs %<span></span>VERSION%, %<span></span>USER% et %<span></span>REPO% par les valeurs réelles.
   - Génère et commit le fichier `README.md` final.

> **Note :** Si vous souhaitez modifier la présentation ou ajouter une section, faites-le dans **`README.template.md`**.

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

Les **GitHub Actions** automatisent le flux de travail. À chaque fois qu du code est envoyé (`git push`), un serveur distant exécute le tests, vérifie le style de code et met à jour la documentation.

### 5.1. Configuration des workflows.

Intégrer les fichier de Workflows au dossier `.github/workflows/` à la racine du projet.

#### 5.1.1. Workflow de tests.

Pour les tests, on uttilise pytest et pytest-cov, et on génère un rapport de couverture dans la console.

```yaml
name: Python Tests
on:
  push:
    branches: [ main, dev , 'feat/**']  # Branch to survey

permissions:
  contents: write
  pages: write
  id-token: write

jobs:
  build:
    runs-on: ubuntu-latest
    strategy:
        matrix:
            python-version: ["3.11"]
    steps:
      - name: Checkout code
        uses: actions/checkout@v5

      - name: Install uv
        uses: astral-sh/setup-uv@v4
        with:
          enable-cache: true
          cache-dependency-glob: "uv.lock"

      - name: Set up Python ${{ matrix.python-version }}
        run: uv python install ${{ matrix.python-version }}

      - name: Install dependencies
        run: uv sync --frozen --all-extras

      - name: Run all tests
        run: uv run pytest --cov=app --cov-report=term-missing > pytest_report.txt
```

#### 5.1.2. Workflow de documentation.
Pour la documentation, on génère les fichiers .rst à partir du code source, puis on compile le HTML et on le déploie sur GitHub Pages.

```yaml
name: Deploy Documentation


on:
  push:
    branches: [main]


permissions:
  contents: write
  pages: write
  id-token: write


jobs:
  build-docs:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Install uv
        uses: astral-sh/setup-uv@v5
        with:
          version: "latest"

      - name: Install dependencies
        run: uv sync --all-extras 
      - name: Debug - Look for app folder
        run: |
          echo "--- Emplacement actuel ---"
          pwd
          echo "--- Liste des fichiers à la racine ---"
          ls -F
          echo "--- Recherche du dossier app ---"
          find . -maxdepth 2 -type d -name "app"
          
      - name: Generate API skeleton
        run: |
          mkdir -p docs/source
          # On cible le dossier 'app' qui contient ton code
          # -f : force la régénération des fichiers .rst
          uv run sphinx-apidoc -f -o docs/source ./app

      # 2. GÉNÉRER LE HTML
      - name: Build Sphinx Documentation
        run: |
          mkdir -p public
          # -n : mode "nitpicky" (signale toutes les petites erreurs)
          # -v : mode verbeux (affiche ce que Sphinx fait)
          uv run sphinx-build -nv -b html docs/source public

      - name: Upload artifact
        uses: actions/upload-pages-artifact@v3
        with:
          path: 'public'

  deploy-docs:
    needs: build-docs
    runs-on: ubuntu-latest
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    steps:
      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v4
```

#### 5.1.3. Workflow de linting (Ruff).

Pour le Workflow de Linting, on utilise Ruff pour vérifier le style de code et corriger automatiquement les problèmes détectés.

```yaml
name: Python Ruff
on:
  push:
    branches: [ main, dev , 'feat/**']  # Branch to survey

permissions:
  contents: write
  pages: write
  id-token: write

jobs:
  build:
    runs-on: ubuntu-latest
    strategy:
        matrix:
            python-version: ["3.11"]
    steps:
      - name: Checkout code
        uses: actions/checkout@v5

      - name: Install uv
        uses: astral-sh/setup-uv@v4
        with:
          enable-cache: true
          cache-dependency-glob: "uv.lock"

      - name: Set up Python ${{ matrix.python-version }}
        run: uv python install ${{ matrix.python-version }}

      - name: Install dependencies
        run: uv sync --frozen --all-extras

      - name: Run Ruff Check
        # Vérifie les erreurs de code et de logique
        run: uv run ruff check .

      - name: Run Ruff Format
        # Vérifie que le code est bien formaté (équivalent de Black)
        run: uv run ruff format --check .
```

### 5.2 Activation sur Github 

Pour que le déploiement fonctionne, GitHub Actions doit être autorisé à publier des pages :
Il faut donc suivre ces étapes à partir du Repository en ligne
* **Cliquer sur le button Settings** (en haut à droite dans la barre de menu).
* **Cliquer sur Pages** dans le menu de gauche
* **Selectionner "GitHub Actions"** à la place de "Deploy from a branch" dans la section Build and deployment > Source

La documentation sera alors accessible à l'adresse : https://%USER%.github.io/%REPO%/

## 6. Docker & CI/CD

Ce projet est entièrement conteneurisé et configuré pour un déploiement continu (CD).

### Architecture de déploiement:

- **Image de base :** `python:3.11-slim` (pour la compatibilité Pandas/Numpy)
- **Gestionnaire :** [uv](https://github.com/astral-sh/uv) pour des builds ultra-rapides.
- **CI/CD :** GitHub Actions (Tests Pytest -> Build Docker -> Push Docker Hub).
- **Mise à jour :** Watchtower (détection automatique des nouvelles images sur le serveur).

### Lancement local (Développement)

Si vous voulez lancer l'application avec Docker sur votre machine :

1. **Build de l'image :**
   ```bash
   docker build -t mon-app-python .
   ```

2. **Lancement du conteneur :**
  ```bash
  docker run -d -p 8080:5000 --name $DOCKER_CONTENEUR mon-app-python
  ```

L'application sera accessible sur http://localhost:8080

Vous pouvez lancer un autre port que 8080 pour lancer le conteneur sur le serveur.

3. **Vérification des logs :**
  ```bash
  docker logs -f $DOCKER_CONTENEUR
  ```

### Déploiement en Production (Serveur):

Le déploiement est automatisé via GitHub Actions et Docker Compose.

1. Configuration initiale du serveur
* Installez Docker et Docker Compose sur votre VPS.
* Copiez uniquement le fichier docker-compose.yml dans un dossier dédié (ex: /var/www/mon-app/).
* Créer un fichier .env à la racine du projet : 

  ```bash
  DOCKER_USER=votre_pseudo
  DOCKER_CONTENEUR=nom_de_l_image
  APP_PORT=80
  ```

1. Lancement de la Stack
  ```bash
  docker compose up -d
  ```

Cela lancera simultanément :

* L'application Python : accessible sur le port 80.
* Watchtower : qui vérifiera toutes les 5 minutes sur Docker Hub si une nouvelle image est disponible pour redéployer l'app automatiquement.

### Maintenance et Suppression :

Voici les commandes pour gérer le cycle de vie de l'application :

1. **Arrêter l'application sans supprimer les ressources:**
  ```bash
  docker compose stop
  ```
2. **Arrêter l'application en supprimant le contener et le réseaux:**
  ```bash
  docker compose down
  ```

3. **Supprimer l'image de l'application:**
  ```bash
  docker rmi fatman3194/mon-app-python
  docker rmi containrrr/watchtower
  ```
  
4. **Nettoyage complet (recommandé si l'espace disque est saturé) :**
  ```bash
  docker compose stop
  docker system prune
  ```