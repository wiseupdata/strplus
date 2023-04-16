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
    "base_url": "https://wiseupdata.github.io/strplus/",
    "repo_url": "https://github.com/wiseupdata/strplus/",
    "repo_name": "STRPLUS",
    "globaltoc_depth": 3,
    "color_primary": "pink",
    "color_accent": "gray",
    "logo_icon": "&#xe869",
    "nav_links": [
        {"href": "https://wiseupdata.github.io/strplus/", "title": "HOME", "internal": True},
        {"href": "https://github.com/wiseupdata", "title": "GitHub", "internal": False},
        {"href": "https://wiseupdata.com", "title": "Site", "internal": False},
    ],
}

html_static_path = ["_static"]

# Add custom CSS file
html_css_files = ["style.css"]
