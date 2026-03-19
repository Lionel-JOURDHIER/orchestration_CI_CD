# Architecture de base ToolBox

Ce projet orchestration_CI_CD est en version  et appartient à Lionel-JOURDHIER.

[![Documentation](https://img.shields.io/badge/Documentation-GitHub%20Pages-blue?logo=github&logoColor=white)](https://Lionel-JOURDHIER.github.io/orchestration_CI_CD/) [![Code](https://img.shields.io/badge/Code--181717?logo=github)](https://github.com/Lionel-JOURDHIER/orchestration_CI_CD) ![Deploy Documentation](https://github.com/Lionel-JOURDHIER/orchestration_CI_CD/actions/workflows/documentation.yml/badge.svg) [![Python Tests](https://github.com/Lionel-JOURDHIER/orchestration_CI_CD/actions/workflows/test.yml/badge.svg)](https://github.com/Lionel-JOURDHIER/orchestration_CI_CD/actions)  [![Ruff Status](https://github.com/Lionel-JOURDHIER/orchestration_CI_CD/actions/workflows/ruff.yml/badge.svg)](https://github.com/Lionel-JOURDHIER/orchestration_CI_CD/actions) ![Security Audit](https://img.shields.io/badge/Security-Audit_Passed-green?logo=github-actions&logoColor=white) ![Ruff](https://img.shields.io/badge/Ruff-checked-green?logo=ruff&logoColor=white)
![Python](https://img.shields.io/badge/python-3.11-blue.svg)  ![Linter](https://img.shields.io/badge/linter-ruff-orange.svg)  ![License](https://img.shields.io/badge/license-MIT-green.svg) ![uv](https://img.shields.io/badge/managed%20by-uv-de5b41.svg) ![Docker](https://img.shields.io/badge/docker-ready-blue.svg?logo=docker) ![Last Commit](https://img.shields.io/github/last-commit/Lionel-JOURDHIER/orchestration_CI_CD) ![Repo Size](https://img.shields.io/github/repo-size/Lionel-JOURDHIER/orchestration_CI_CD) ![Open Issues](https://img.shields.io/github/issues/Lionel-JOURDHIER/orchestration_CI_CD)
![Contributeurs](https://img.shields.io/github/contributors/Lionel-JOURDHIER/orchestration_CI_CD?logo=github&color=orange)

### Liste des contributeurs
[![Contributeurs](https://contrib.rocks/image?repo=Lionel-JOURDHIER/orchestration_CI_CD)](https://github.com/Lionel-JOURDHIER/orchestration_CI_CD/graphs/contributors)

`docker compose -f docker-compose.prod.yml pull`
`docker compose -f docker-compose.prod.yml up`

---
## Quickstart : Orchestrateur CI CD

Ce guide cous permet d'uttiliser l'orchestrateur pour lier un front et une base de donnée postgres en back via une API. 

### 1. Installation rapide

L'utilisation de `uv` est recommandée pour une installation ultra-rapide des dépendances.

```bash
git clone [https://github.com/Lionel-JOURDHIER/orchestration_CI_CD.git](https://github.com/Lionel-JOURDHIER/orchestration_CI_CD.git) && cd orchestration_CI_CD

uv sync --project app_front # cd app_front && uv sync && cd ..

uv sync --project app_api # cd app_api && uv sync && cd ..

uv sync --project docs # cd docs && uv sync && cd ..
```

### 2. Création des contener en local

Pour créer les conteneurs, utilisez la commande suivante :

```bash
docker compose build && docker compose up
```

### 2. Création des conteners dockers depuis le repository docker online (dernière version)

Pour créer les conteneurs, utilisez la commande suivante :

```bash
docker compose -f docker-compose.prod.yml pull
docker compose -f docker-compose.prod.yml up
```

## Uttilisation de l'application

Les adresses sont celle definis dans le fichier .env. Vous pouvez utiliser les adresses pour tester la fonctionnalité de prédiction.

API (Swagger) : http://localhost:9090/docs

Frontend Streamlit : http://localhost:8501

### Architecture : 

```plaintext
.
├── .github/
│   ├── workflows/
│   │   ├── deploy_docker.yml         # Docker 
│   │   ├── documentation.yml         # Documentation  
│   │   ├── extract.yml               # Extract information depuis le repo pour compléter le README
│   │   ├── ruff.yml                  # lintage 
│   │   ├── secrets.yml               # verifie la présence de secret dans le code
│   │   └── test.yml                  # execute les test pour le code 
│   ├── CONTRIBUTING.template.md
│   ├── CONTRIBUTING.md
│   ├── CODE_OF_CONDUCT.template.md
│   └── CODE_OF_CONDUCT.md
├── app_front/             # Service Streamlit
│   ├── main.py
│   ├── pages
│   │   ├── 0_insert.py
│   │   └── 1_read.py  
│   ├── pyproject.toml
│   ├── uv.lock
│   └── Dockerfile
├── app_api/               # Service FastAPI
│   ├── Dockerfile
│   ├── pyproject.toml
│   ├── uv.lock
│   ├── models/            # Dossier contenant le modèle pydantic
│   │   ├── __init__.py
│   │   └── models.py      # modèle pydantic
│   ├── modules/           # Dossier contenant la logique du projet 2
│   │   ├── __init__.py
│   │   └── db_tools.py     # Contient les operations de connexion et de CRUD
│   ├── maths/             # Dossier contenant la logique du projet 1
│   │   ├── __init__.py
│   │   └── mon_module.py  # Contient les fonctions add, sub, square, print_data
│   ├── data/              # Dossier contenant les data du projet 1
│   │   └── moncsv.csv     # Données d'entrée pour la démonstration
│   └── main.py            # Point d'entrée de l'application
├── tests/
│   ├── test_api.py
│   ├── test_front_1_read.py
│   ├── test_front_app_front/py
│   └── test_front_0_insert.py
├── docker-compose.yml         # Pour le développement (build: .)
├── docker-compose.prod.yml    # Pour la prod (image: user/repo:tag)
├── pytest.ini
├── .gitignore
├── .dockerignore
├── README.md
├── README.template.md
└── .env.example
 

```

### Maintenance et Suppression :

Voici les commandes pour gérer le cycle de vie de l'application :

1. **Arrêter l'application sans supprimer les ressources:**
  ```bash
  docker compose stop
  ```
2. **Arrêter l'application en supprimant le contener, le réseaux et les images:**
  ```bash
  docker compose down --rmi all
  ```

3. **Supprimer l'image de l'application:**
  ```bash

  ```

4. **Nettoyage complet (recommandé si l'espace disque est saturé) :**
  ```bash
  docker compose stop
  docker system prune
  ```