import os
import sys

sys.path.insert(0, os.path.abspath("../.."))
pygments_style = "monokai"

project = "strplus"
copyright = "2023, WiseUpData"
author = "WiseUpData"
release = "1.0.2"

extensions = ["sphinx.ext.autodoc", "sphinx.ext.doctest", "sphinx.ext.extlinks", "sphinx.ext.intersphinx", "sphinx.ext.todo", "sphinx.ext.mathjax", "sphinx.ext.viewcode", "sphinx_copybutton"]


autosummary_generate = True
autoclass_content = "class"


templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
html_show_sourcelink = True

html_theme = "sphinx_material"

html_theme_options = {
    "base_url": "https://wiseupdata.github.io/strplus/",
    "repo_url": "https://github.com/wiseupdata/strplus/",
    "repo_name": "STRPLUS",
    "globaltoc_depth": -1,
    "theme_color": "e92164",
    "color_primary": "pink",
    "css_minify": True,
    "repo_type": "github",
    "color_accent": "teal",
    # "logo_icon": "&#xe021",
    "logo_icon": "&#xE88A",
    "nav_title": "strplus package",
    "nav_links": [
        {"href": "https://wiseupdata.github.io/strplus/", "title": "Home", "internal": False},
        {"href": "https://github.com/wiseupdata/strplus", "title": "GitHub", "internal": False},
        {"href": "https://github.com/wiseupdata", "title": "GitHub Site", "internal": False},
        {"href": "https://wiseupdata.com", "title": "Site", "internal": False},
    ],
    "heroes": {"index": "Extend your string powers with Str+", "customization": "Good function to use like the natives ones!"},
    "table_classes": ["plain"],
}

html_sidebars = {"**": ["meu_template.html", "logo-text.html", "globaltoc.html", "localtoc.html", "searchbox.html"]}

# html_sidebars = {
#     "**": ["meu_template.html"]
# }

html_static_path = ["_static"]
html_use_index = True
html_domain_indices = True
todo_include_todos = True
html_use_index = True

# Add custom CSS file
html_css_files = ["style.css"]
