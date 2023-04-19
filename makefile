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
	@echo "under construction"
# Tasks: Run `make format` or `make lint` to manually run each of the steps

format: black isort
lint: black-lint isort-lint flake8-lint

#use Example:
# make path=strplus/functions.py
# make 