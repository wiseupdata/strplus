# Default path
path ?= .

make: format-black format-isort test

# Automatic code formatting
format-black:
	@black --line-length 200 --skip-magic-trailing-comma $(path)

# Linting tasks
lint-black:
	@black --line-length 200 --skip-magic-trailing-comma $(path) --check

format-isort:
	@isort .

lint-isort:
	@isort . --check

lint-flake8:
	@flake8 .

# Test and coverage tasks
test:
	@rm -rf htmlcov/
	@pytest --cov=$(path) --cov-report html tests/
	@pytest --cov=$(path) tests/

coverage-html:
	@rm -rf htmlcov/
	@pytest --cov=$(path) --cov-report html tests/

# Clean tasks
htmlclean:
	@rm -rf htmlcov/

# Tasks: Run `make format` or `make lint` to manually run each of the steps
format: format-black format-isort
lint: lint-black lint-isort lint-flake8

#use Example:
# make path=strplus/functions.py
# make 