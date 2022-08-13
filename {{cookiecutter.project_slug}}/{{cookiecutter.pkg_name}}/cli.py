"""Console script for {{cookiecutter.pkg_name}}."""

{% if cookiecutter.command_line_interface|lower == 'click' -%}
import logging
import os
import sys

import click

from {{cookiecutter.pkg_name}} import __version__

from typing import Any, Dict

FORMATTERS = {
    "DEBUG": {"format": "%(asctime)s - %(levelname)s - %(name)s - %(funcName)s - %(message)s"},
    "INFO": {"format": "%(asctime)s - %(levelname)s - %(message)s"},
    "WARNING": {"format": "%(asctime)s - %(levelname)s - %(message)s"},
    "ERROR": {"format": "%(asctime)s - %(levelname)s - %(name)s - %(message)s"},
    "CRITICAL": {"format": "%(asctime)s - %(levelname)s - %(name)s - %(message)s"},
}

HANDLERS_BASE = {
    "console": {
        "class": "logging.StreamHandler",
        "formatter": "INFO",
        "stream": "ext://sys.stdout",
    },
    "file": {
        "class": "logging.FileHandler",
        "formatter": "INFO",
        "filename": "app.log",
    },
}


def get_log_config(name: str, log_level: str = "INFO", log_file: str | None = None) -> Dict[str, Any]:
    """Return a dict usable in dictConfig
    Set up logging to stdout with ``log_level``. If ``log_file`` is given use it instead.
    """

    if log_file is not None:
        handlers = {"handler": HANDLERS_BASE["file"]}
        handlers["handler"]["filename"] = log_file
    else:
        handlers = {"handler": HANDLERS_BASE["console"]}
    handlers["console"] = HANDLERS_BASE["console"]

    handlers["handler"]["formatter"] = log_level
    log_conf = {"level": log_level, "handlers": ["handler"]}

    res = {
        "version": 1,
        "formatters": FORMATTERS,
        "handlers": handlers,
        "loggers": {
            name: log_conf,
            # "asyncio": log_conf,
            # "root": log_conf,
            # "uvicorn": {"level": "INFO", "handlers": ["console", "handler"]},
        },
    }

    return res

logger = logging.getLogger("{{cookiecutter.pkg_name}}")


def version_msg() -> str:
    """Return the version, location and Python powering it."""
    python_version = sys.version
    location = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    message = "{{ cookiecutter.project_name }} %(version)s from {} (Python {})"
    return message.format(location, python_version)

@click.group(context_settings=dict(help_option_names=["-h", "--help"]))
@click.pass_context
@click.version_option(__version__, "-V", "--version", message=version_msg())
@click.option("-v", "--verbose", is_flag=True, help="Force all log levels to debug", default=False)
@click.option(
    "--log-file",
    type=click.Path(dir_okay=False, writable=True),
    default=None,
    help="File to be used for logging",
)
@click.option(
    "--log-level",
    type=click.Choice(
        [
            "DEBUG",
            "INFO",
            "WARNING",
            "ERROR",
            "CRITICAL",
        ],
        case_sensitive=False,
    ),
    help="Log level",
    default="INFO",
    show_default=True,
)
def cli(
    ctx: click.Context,
    log_file: str,
    log_level: str,
    verbose: bool,
) -> None:
    """Main entry point"""
    logging.dictConfig(
        get_log_config(
            "{{cookiecutter.pkg_name}}",
            log_level=log_level if not verbose else "DEBUG",
            log_file=log_file,
        )
    )
    logger.debug("Init cli successful")

@click.command()
def main():
    """Main entrypoint."""
    click.echo("{{ cookiecutter.project_slug }}")
    click.echo("=" * len("{{ cookiecutter.project_slug }}"))
    click.echo("{{ cookiecutter.project_short_description }}")


def run_cli():
    cli(auto_envvar_prefix="{{cookiecutter.pkg_name|upper}}")


if __name__ == "__main__":
    run_cli()  # pragma: no cover

{%- endif %}
