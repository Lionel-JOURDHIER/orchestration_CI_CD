# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os
import sys

sys.path.insert(0, os.path.abspath("../../"))

project = "Ocrchestration"
copyright = "2026, Lionel-JOURDHIER"
author = "Lionel-JOURDHIER"
release = "2026"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",  # INDISPENSABLE : extrait la doc des docstrings
    "sphinx.ext.napoleon",  # Supporte le format Google/NumPy (plus lisible)
    "sphinx.ext.viewcode",  # Ajoute un lien [source] à côté de tes fonctions
    "sphinx.ext.mathjax",  # Pour le rendu des formules LaTeX
    "myst_parser",  # Pour lire les fichiers .md (README, etc.)
    "sphinxcontrib.bibtex",  # Pour la gestion du fichier .bib
]
bibtex_bibfiles = ["refs.bib"]

templates_path = ["_templates"]
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "furo"
html_static_path = ["_static"]
