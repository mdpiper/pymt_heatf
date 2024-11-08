.PHONY: clean clean-test clean-pyc clean-build docs help
.DEFAULT_GOAL := help

define BROWSER_PYSCRIPT
import os, webbrowser, sys

try:
	from urllib import pathname2url
except:
	from urllib.request import pathname2url

webbrowser.open("file://" + pathname2url(os.path.abspath(sys.argv[1])))
endef
export BROWSER_PYSCRIPT

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT

BROWSER := python -c "$$BROWSER_PYSCRIPT"

help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

clean: clean-build clean-compile clean-pyc clean-test ## remove all build, test, coverage and Python artifacts

clean-build: ## remove build artifacts
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-compile: ## remove compilation artifacts
	find . -name '*.c' -exec rm -f {} +
	find . -name '*.mod' -exec rm -f {} +
	find . -name '*.o' -exec rm -f {} +
	find . -name '*.so' -exec rm -f {} +
	rm -fr build/

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test: ## remove test and coverage artifacts
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/
	rm -fr .pytest_cache

lint: ## check style with ruff
	ruff check .

pretty:
	find pymt_heatf -name '*.py' | xargs isort
	black . --check

test: ## run tests quickly with the default Python
	bmi-test pymt_heatf.bmi:HeatModelF --config-file=${PWD}/examples/test.cfg --root-dir=examples -vvv

test-all: ## run tests on every Python version with tox
	tox

coverage: ## check code coverage quickly with the default Python
	coverage run --source pymt_heatf -m pytest
	coverage report -m
	coverage html
	$(BROWSER) htmlcov/index.html

release: dist ## package and upload a release
	twine upload dist/*

dist: clean ## builds source and wheel package
	python -m build --no-isolation
	ls -l dist

install: clean ## install the package to the active Python's site-packages
	pip install meson meson-python ninja
	pip install --no-build-isolation --editable .
