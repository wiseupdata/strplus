# Variables
PROJECT_DIR = .

# Commands

test:
    pytest --cov=$(PROJECT_DIR) tests/

cover:
    rm -rf htmlcov/
    pytest --cov=$(PROJECT_DIR) --cov-report html tests/
