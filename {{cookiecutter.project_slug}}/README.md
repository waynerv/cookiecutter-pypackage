{% set is_open_source = cookiecutter.open_source_license != 'Not open source' -%}
# {{ cookiecutter.project_name }}

{% if is_open_source -%}
[![pypi](https://img.shields.io/pypi/v/{{ cookiecutter.project_slug }}.svg)](https://pypi.org/project/{{ cookiecutter.project_slug }}/)
[![python](https://img.shields.io/pypi/pyversions/{{ cookiecutter.project_slug }}.svg)](https://pypi.org/project/{{ cookiecutter.project_slug }}/)
[![Build Status](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/actions/workflows/push.yml/badge.svg)](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/actions/workflows/push.yml)
[![codecov](https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/branch/main/graphs/badge.svg)](https://codecov.io/github/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }})
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
{% else -%}
{% endif -%}

{{ cookiecutter.project_short_description }}

{% if is_open_source -%}
* Documentation: <https://{{ cookiecutter.github_username }}.github.io/{{ cookiecutter.project_slug }}>
* GitHub: <https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}>
* PyPI: <https://pypi.org/project/{{ cookiecutter.project_slug }}/>
* Free software: {{ cookiecutter.open_source_license }}
{% endif -%}

## Installation
{%- if is_open_source %}

Using a python environment running python >= 3.8:

```shell
$ pip install {{ cookiecutter.project_slug }}
```
{% else %}
Refer to the [section of the documentation on contributing](https://{{ cookiecutter.github_username }}.github.io/{{ cookiecutter.project_slug }}/contributing/)
{% endif -%}

## Usage

Checkout the [section of the documentation on usage](https://{{ cookiecutter.github_username }}.github.io/{{ cookiecutter.project_slug }}/usage/)

## Contributing

We encourage contributions and credit is always given! Please have a look at the [section of the documentation on contributing](https://{{ cookiecutter.github_username }}.github.io/{{ cookiecutter.project_slug }}/contributing/) or ``CONTRIBUTING.md`` file.
