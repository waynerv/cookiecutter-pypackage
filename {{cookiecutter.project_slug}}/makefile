.DEFAULT_GOAL := help

sources = {{ cookiecutter.pkg_name }}

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT

.PHONY: help
help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

.PHONY: clean
clean: clean-build clean-pyc clean-test ## remove all build, test, coverage and Python artifacts

.PHONY: clean-build
clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +
	find . -name '.mypy_cache' -exec rm -fr {} +
	find . -name 'requirements-*.txt' -exec rm -fr {} +

.PHONY: clean-pyc
clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

.PHONY: clean-test
clean-test: ## remove test and coverage artifacts
	rm -f .coverage
	rm -f coverage.xml
	rm -fr htmlcov/
	rm -fr .pytest_cache
	rm -fr testtemp/

.PHONY: format
format:
	isort $(sources) tests
	black $(sources) tests

.PHONY: lint
lint:
	flake8 $(sources) tests
	{%- if cookiecutter.use_mypy == 'y' %}
	mypy $(sources) tests
	{%- endif %}

.PHONY: test
test: format lint unittest

.PHONY: unittest
unittest:
	pytest

.PHONY: coverage
coverage:
	pytest --cov=$(sources) --cov-branch --cov-report=term-missing tests

.PHONY: pre-commit
pre-commit:
	pre-commit run --all-files
