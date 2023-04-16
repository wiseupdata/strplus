# Default path
path ?= .

make: black isort test

# Automatic code formatting
black:
	@black --line-length 200 --skip-magic-trailing-comma $(path)

# Linting tasks
black-lint:
	@black --line-length 200 --skip-magic-trailing-comma $(path) --check

isort:
	@isort .

isort-lint:
	@isort . --check

# Test and coverage tasks
test:
	@rm -rf htmlcov/
	@pytest --cov=$(path) --cov-report html tests/
	@pytest --cov=$(path) tests/

coverage:
	@rm -rf htmlcov/
	@pytest --cov=$(path) --cov-report html tests/

# Clean tasks
htmlclean:
	@rm -rf htmlcov/

# Generate the documentation
doc:
	@find sphinx/source/ -type f -name "*.rst" ! -name "index.rst" -delete
	@poetry run sphinx-apidoc -f -o sphinx/source/ ./strplus
	@rm -Rf sphinx/build/html
	@poetry run sphinx-build -b html sphinx/source/ sphinx/build/html
	@rm -Rf docs && mkdir docs && touch docs/.nojekyll
	@cp -r sphinx/build/html/* ./docs/        

# Tasks: Run `make format` or `make lint` to manually run each of the steps
format: black isort
lint: black-lint isort-lint flake8-lint

#use Example:
# make path=strplus/functions.py
# make 