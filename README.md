# Cookiecutter PyPackage

Cookiecutter template for a Python package, built with popular develop tools and
conform to best practice.

[![CI Status](https://github.com/mishamsk/cookiecutter-pypackage/actions/workflows/dev.yml/badge.svg)](https://github.com/mishamsk/cookiecutter-pypackage/actions/workflows/dev.yml)
[![License](https://img.shields.io/pypi/l/ppw)](https://opensource.org/licenses/BSD-2-Clause)

* Documentation: <https://mishamsk.github.io/cookiecutter-pypackage>

## Features

This tool will create Python project with the following features:

* [Poetry](https://python-poetry.org/): Manage dependency, build and release
* Makefile template for typical operations
* [Mkdocs](https://www.mkdocs.org): Writing your docs in markdown style
* Testing with [Pytest](https://pytest.org) (unittest is still supported out of the box)
* [Tox](https://tox.readthedocs.io): Test your code against environment matrix, lint and artifact check
* Format with [Black](https://github.com/psf/black) and [Isort](https://github.com/PyCQA/isort)
* Lint code with [Flake8](https://flake8.pycqa.org)
* Check static type with [Mypy](http://mypy-lang.org/) (optional)
* [Pre-commit hooks](https://pre-commit.com/): Formatting/linting anytime when commit your code
* [Mkdocstrings](https://mkdocstrings.github.io/): Auto API doc generation
* Command line interface using [Click](https://click.palletsprojects.com/en/8.0.x/) (optional)
* [bump2version](https://github.com/c4urself/bump2version): Pre-configured version bumping with a single command
* Continuous Integration/Deployment by [GitHub actions](https://github.com/features/actions), includes:
    - publish dev build/official release to TestPyPI/PyPI automatically when CI success
    - publish documents automatically when CI success
    - extract changelog from CHANGELOG and integrate with release notes automatically
* Host your documentation from [GitHub Pages](https://pages.github.com) with zero-config

## Quickstart

Install the latest Cookiecutter if you haven't installed it yet (see instruction [here](https://cookiecutter.readthedocs.io/en/stable/installation.html)). I suggest using [pipx](https://github.com/pypa/pipx) to make it a global tool in an isolated Python environment
```
pipx install cookiecutter
```

Generate a Python package project:
```
cookiecutter https://github.com/mishamsk/cookiecutter-pypackage
```

And code away!

## Cookiecutter options

`project_name`
The name of your new Python package project. This is used in
documentation, so spaces and any characters are fine here.

`project_slug`
The name of your Python package for PyPI, also as the repository name of GitHub.
Typically, it is the slugified version of project_name.

`pkg_name`
The namespace of your Python package. This should be Python import-friendly.

`project_short_description`
A 1-sentence description of what your Python package does.

`full_name`
Your full name.

`email`
Your email address.

`github_username`
Your GitHub username.

`version`
The starting version number of the package.

`use_mypy`
If use mypy for static type check in pre-commit hooks and tox.

`install_precommit_hooks`
If you choose yes, then cookiecutter will install pre-commit hooks for you.

`docstrings_style`
one of `google, numpy, pep257`. It's required by flake8-docstrings.

`command_line_interface`
Whether to create a console script using Python Click. Console script
entry point will match the project_slug. Options: \['click', "No
command-line interface"\]

## CI/CD setup
Except the settings above, you'll also need configure gitub repsitory secrets at page repo > settings > secrtes, and add the following secrets:
- TEST_PYPI_API_TOKEN (required for publishing dev release to testpypi)
- PYPI_API_TOKEN (required for publish )

# Credits

This repo is forked from [waynerv/cookiecutter-pypackage](https://github.com/mishamsk/cookiecutter-pypackage), whose origin traces all the way to [audreyfeldroy/cookiecutter-pypackage](https://github.com/audreyfeldroy/cookiecutter-pypackage)
