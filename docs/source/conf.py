# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys

sys.path.insert(0, os.path.abspath("../.."))
sys.path.append(os.path.abspath("./_pygments"))
pygments_style = "monokai"

project = "strplus"
copyright = "2023, WiseUpData"
author = "WiseUpData"
release = "0.0.7"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration
extensions = ["sphinx.ext.autodoc", "sphinx.ext.viewcode", "sphinx.ext.todo"]

templates_path = ["_templates"]
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = "yummy_sphinx_theme"
html_theme = "sphinx_material"
html_theme_options = {
    "color_primary": "blue",
    "color_accent": "light-blue",
    "nav_title": "My Documentation",
    "nav_links": [("Home", "index"), ("Examples", "examples")],
    "globaltoc_depth": 2,
    "globaltoc_includehidden": True,
    "master_doc": False,
    # 'nav_item_classes': [('navbar-1', 'navbar-item'), ('navbar-2', 'navbar-item')],
}

# sphinx_material.extend(
#     'blue',
#     logo='path/to/your/logo.png',
#     palette={
#         'primary': 'blue',
#         'accent': 'light-blue',
#         'background': 'white',
#     },
#     favicon='path/to/your/favicon.ico',
#     # Include custom CSS
#     extra_css=[
#         'path/to/custom.css',
#     ],
# )

html_static_path = ["_static"]
