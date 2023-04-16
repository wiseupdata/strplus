# Default path
path ?= .

# Automatic code formatting
format-black:
	@black --line-length 200 --skip-magic-trailing-comma $(path)

format-isort:
	@isort .

# Linting tasks
lint-black:
	@black --line-length 200 --skip-magic-trailing-comma $(path) --check

lint-isort:
	@isort . --check

lint-flake8:
	@flake8 .

# Test and coverage tasks
test:
	@rm -rf htmlcov/
	@pytest --cov=$(path) tests/
	@pytest --cov=$(path) --cov-report html tests/

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