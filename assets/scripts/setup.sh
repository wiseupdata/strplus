
ls /home/silvio/.cache/pypoetry/virtualenvs/

rm -Rf /home/silvio/.cache/pypoetry/virtualenvs/strplus*
rm poetry.lock
poetry install
poetry shell


poetry add --group dev mkdocs
poetry add --group dev mkdocstrings[python]
poetry add --group dev mkdocs-gen-files
poetry add --group dev mkdocs-literate-nav
poetry add --group dev mkdocs-section-index
poetry add --group dev mkdocs-material
poetry add --group dev mkdocs-material-extensions
poetry add --group dev mkdocs-jupyter

mkdocs new .
mkdocs serve

mkdocs build
touch docs/.nojekyll

poetry run python scripts/gen_ref_pages.py


