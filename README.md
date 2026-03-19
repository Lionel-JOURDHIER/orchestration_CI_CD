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
# Cloner et entrer dans le projet
git clone [https://github.com/Lionel-JOURDHIER/orchestration_CI_CD.git](https://github.com/Lionel-JOURDHIER/orchestration_CI_CD.git) && cd orchestration_CI_CD

# Créer l'environnement virtuel pour la partie front
uv sync --project app_front # cd app_front && uv sync && cd ..

# Créer l'environnement virtuel pour la partie api
uv sync --project app_api # cd app_api && uv sync && cd ..

# Créer l'environnement virtuel pour la documentation automatique
uv sync --project docs # cd docs && uv sync && cd ..
```

### 2. Execution du programme

Pour exécuter le programme tout en garantissant la résolution des imports :

```bash
# Via l'environnement activé
python -m app.main

# OU directement avec uv (sans activation préalable)
uv run python -m app.main
```


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
2. **Arrêter l'application en supprimant le contener, le réseaux et les images:**
  ```bash
  docker-compose down --rmi all
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