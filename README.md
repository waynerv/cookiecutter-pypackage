# Cookiecutter PyPackage

Cookiecutter template for a Python package, built with popular develop tools and
conform to best practice.

[![CI Status][ci_badge]](ci_url)
[![License][license_badge]](license_url)

* Documentation: <https://hainesm6-learning.github.io/cookiecutter-pypackage/>

## Features

This tool will create Python project with the following features:

* [Poetry](https://python-poetry.org/): Manage dependency, build and release
* [Mkdocs](https://www.mkdocs.org): Writing your docs in markdown style
* Testing with [Pytest](https://pytest.org) (unittest is still supported out of the box)
* Code coverage report and endorsed by [Codecov](https://codecov.io)
* [Tox](https://tox.readthedocs.io): Test your code against environment matrix, lint and artifact check
* Format with [Black](https://github.com/psf/black) and [Isort](https://github.com/PyCQA/isort)
* Lint code with [Flake8](https://flake8.pycqa.org) and [Flake8-docstrings](https://pypi.org/project/flake8-docstrings/)
* Check static type with [Mypy](http://mypy-lang.org/) (optional)
* [Pre-commit hooks](https://pre-commit.com/): Formatting/linting anytime when commit your code
* [Mkdocstrings](https://mkdocstrings.github.io/): Auto API doc generation
* Command line interface using [Click](https://click.palletsprojects.com/en/8.0.x/) (optional)
* Continuous Integration/Deployment by [GitHub actions](https://github.com/features/actions), includes:
    - publish dev build/official release to TestPyPI/PyPI
    - publish documents automatically when CI success
* Host your documentation from [GitHub Pages](https://pages.github.com) with zero-config

## Quickstart

Install the latest Cookiecutter if you haven't installed it yet ([guidelines for installation](https://cookiecutter.readthedocs.io/en/1.7.2/installation.html)):

Generate a Python package project:

```
cookiecutter https://github.com/hainesm6-learning/cookiecutter-pypackage.git
```

Then follow **[Tutorial](docs/tutorial.md)** to finish other configurations.

# Credits

This repo is forked from [waynerv/cookiecutter-pypackage](https://github.com/waynerv/cookiecutter-pypackage), which itself is a fork, with [audreyfeldroy/cookiecutter-pypackage](https://github.com/audreyfeldroy/cookiecutter-pypackage) being the original.

[ci_badge]: https://github.com/hainesm6-learning/cookiecutter-pypackage/actions/workflows/dev.yml/badge.svg
[ci_url]: https://github.com/hainesm6-learning/cookiecutter-pypackage/actions/workflows/dev.yml
[license_badge]: https://img.shields.io/badge/License-BSD_3--Clause-blue.svg
[license_url]: https://opensource.org/licenses/BSD-3-Clause