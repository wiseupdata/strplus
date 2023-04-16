import os
import sys

sys.path.insert(0, os.path.abspath("../.."))
pygments_style = "monokai"

project = "strplus"
copyright = "2023, WiseUpData"
author = "WiseUpData"
release = "0.0.8"

extensions = ["sphinx.ext.autodoc", "sphinx.ext.viewcode", "sphinx.ext.todo"]

templates_path = ["_templates"]
exclude_patterns = []

html_theme = "sphinx_material"
html_theme_options = {
    "color_primary": "blue",
    "color_accent": "light-blue",
    "nav_title": "My Documentation",
    "nav_links": [("Home", "index"), ("Examples", "examples")],
    "globaltoc_depth": 2,
    "globaltoc_includehidden": True,
    "master_doc": False,
}

html_static_path = ["_static"]
