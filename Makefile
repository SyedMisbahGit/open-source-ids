.PHONY: clean lint test docs run

# Python virtual environment
VENV = venv

# Directories
SRC_DIR = src
TEST_DIR = tests
DOCS_DIR = docs

# Python files
PYTHON_FILES = $(shell find $(SRC_DIR) $(TEST_DIR) -name "*.py")

# Environment variables
export FLASK_APP = src/app.py
export FLASK_ENV = development

# Colors for output
GREEN = \033[0;32m
RED = \033[0;31m
NC = \033[0m

define PRINT
    @printf "\n$(GREEN)%s$(NC)\n\n" "$@"
endef

# Default target
all: clean install lint test

# Create virtual environment
venv:
	@$(PRINT)
	python3 -m venv $(VENV)
	source $(VENV)/bin/activate && pip install --upgrade pip

# Install dependencies
install:
	pip install -r requirements.txt

install-dev:
	pip install -r requirements.txt -r requirements-dev.txt

# Clean build, test, coverage and Python artifacts
clean:
	rm -rf build/ dist/ *.egg-info/ .pytest_cache/ .coverage
	rm -rf .mypy_cache/ .pytest_cache/ htmlcov/
	rm -rf logs/*
	rm -rf data/*
	rm -rf src/migrations/*
	rm -rf deploy/kubernetes/data/*
	rm -rf grafana/provisioning/datasources/*.bak
	rm -rf grafana/provisioning/dashboards/*.bak
	rm -rf prometheus/rules/*.bak
	rm -rf prometheus/*.bak

# Run linters
lint:
	@$(PRINT)
	source $(VENV)/bin/activate && black $(SRC_DIR) $(TEST_DIR)
	source $(VENV)/bin/activate && flake8 $(SRC_DIR) $(TEST_DIR)
	source $(VENV)/bin/activate && mypy $(SRC_DIR) $(TEST_DIR)

# Run tests
.PHONY: test
test:
	@$(PRINT)
	source $(VENV)/bin/activate && pytest --cov=$(SRC_DIR) --cov-report=term-missing

# Generate documentation
docs:
	@$(PRINT)
	source $(VENV)/bin/activate && cd $(DOCS_DIR) && make html

# Run the application
.PHONY: run
run:
	@$(PRINT)
	source $(VENV)/bin/activate && flask run

# Run database migrations
.PHONY: migrate
migrate:
	@$(PRINT)
	source $(VENV)/bin/activate && flask db migrate

# Upgrade database
.PHONY: upgrade
upgrade:
	@$(PRINT)
	source $(VENV)/bin/activate && flask db upgrade

# Downgrade database
.PHONY: downgrade
downgrade:
	@$(PRINT)
	source $(VENV)/bin/activate && flask db downgrade
