# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.2.0] - 2022-08-26

### Changed

- tox won't install all dependencies every time
- tox runs pre-commit for linting & formatting to make sure this is unified
- updated and improved better CICD workflows
- Simplified tutorial

### Fixed

- Removed remnants of codecov docs
- Changelog now uses the proper format

## [0.1.1] - 2022-08-14

### Added

- New: add watch to mkdocs

### Fixed

- Bug: dev cicd workflow dropped with "all" option
- Bug: contributing template missing link to github issues
- Removed old social links from original repo

## [0.1.0] - 2022-08-12

First release, based on https://github.com/waynerv/cookiecutter-pypackage with the following changes:

### Added

- Added makefile
- automatic creation of a package with most recent dependencies

### Changed

- Extended .gitignore
- Updated python test matrix to start from 3.10
- tox refactor
- cicd is optional

### Removed

- Removed deprecated pytest-cookie calls from tests and fixed click test
- Codecov


