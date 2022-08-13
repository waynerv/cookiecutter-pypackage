#!/usr/bin/env python
import os
import subprocess
import sys

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)

import os
import pwd


def get_username():
    return pwd.getpwuid(os.getuid())[0]


def remove_file(filepath):
    try:
        os.remove(os.path.join(PROJECT_DIRECTORY, filepath))
    except FileNotFoundError:
        pass


def execute(*args, supress_exception=False, cwd=None):
    cur_dir = os.getcwd()

    try:
        if cwd:
            os.chdir(cwd)

        proc = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        out, err = proc.communicate()
        out = out.decode("utf-8")
        err = err.decode("utf-8")
        if err and not supress_exception:
            raise Exception(err)
        else:
            return out
    finally:
        os.chdir(cur_dir)


def init_git():
    # print("Initializing git repository")
    if not os.path.exists(os.path.join(PROJECT_DIRECTORY, ".git")):
        execute("git", "config", "--global", "init.defaultBranch", "main", cwd=PROJECT_DIRECTORY)
        execute("git", "init", cwd=PROJECT_DIRECTORY)


def poetry_add_dependencies(use_click: bool, use_mypy: bool):
    # print("Adding dependencies to pyproject.toml")

    if use_click:
        execute("poetry", "add", "click")

    if use_mypy:
        execute("poetry", "add", "--dev", "mypy")

    execute("poetry", "add", "--dev", "pytest")
    execute("poetry", "add", "--dev", "black")
    execute("poetry", "add", "--dev", "flake8")
    execute("poetry", "add", "--dev", "isort")
    execute("poetry", "add", "--dev", "pytest-cov")
    execute("poetry", "add", "--dev", "coverag")
    execute("poetry", "add", "--dev", "bump2version")
    execute("poetry", "add", "--dev", "pre-commit")
    execute("poetry", "add", "--dev", "twine")
    execute("poetry", "add", "--dev", "tox")

    execute("poetry", "add", "--dev", "--optional", "mkdocs")
    execute("poetry", "add", "--dev", "--optional", "mkdocs-include-markdown-plugin")
    execute("poetry", "add", "--dev", "--optional", "mkdocs-material")
    execute("poetry", "add", "--dev", "--optional", "mkdocstrings")
    execute("poetry", "add", "--dev", "--optional", "mkdocs-material-extensions")
    execute("poetry", "add", "--dev", "--optional", "mkdocs-autoref")


def install_pre_commit_hooks():
    execute("poetry", "install")
    execute(sys.executable, "-m", "pre_commit", "install")


if __name__ == "__main__":
    use_click = "{{ cookiecutter.command_line_interface|lower }}" == "click"
    use_mypy = "{{ cookiecutter.use_mypy }}" == "y"
    cicd = "{{ cookiecutter.cicd }}"

    if not use_click:
        cli_file = os.path.join("{{ cookiecutter.pkg_name }}", "cli.py")
        remove_file(cli_file)

    if not cicd == "all":
        preview_file = os.path.join(
            "{{ cookiecutter.pkg_name }}", ".github", "workflows", "preview.yml"
        )
        release_file = os.path.join(
            "{{ cookiecutter.pkg_name }}", ".github", "workflows", "release.yml"
        )
        remove_file(preview_file)
        remove_file(release_file)

    if not cicd == "dev":
        dev_file = os.path.join("{{ cookiecutter.pkg_name }}", ".github", "workflows", "dev.yml")
        remove_file(dev_file)

    if "Not open source" == "{{ cookiecutter.open_source_license }}":
        remove_file("LICENSE")

    try:
        poetry_add_dependencies(use_click, use_mypy)
    except Exception as e:
        print(e)

    try:
        init_git()
    except Exception as e:
        print(e)

    if "{{ cookiecutter.install_precommit_hooks }}" == "y":
        try:
            install_pre_commit_hooks()
        except Exception as e:
            print(str(e))
            print(
                "Failed to install pre-commit hooks. Please run `pre-commit install` by your self. For more on pre-commit, please refer to https://pre-commit.com"
            )
