#!/usr/bin/env python
import os
import subprocess

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
        execute("poetry", "add", "--lock", "click", cwd=PROJECT_DIRECTORY)

    if use_mypy:
        execute("poetry", "add", "--lock", "--dev", "mypy", cwd=PROJECT_DIRECTORY)

    execute("poetry", "add", "--lock", "--dev", "pytest", cwd=PROJECT_DIRECTORY)
    execute("poetry", "add", "--lock", "--dev", "black", cwd=PROJECT_DIRECTORY)
    execute("poetry", "add", "--lock", "--dev", "flake8", cwd=PROJECT_DIRECTORY)
    execute("poetry", "add", "--lock", "--dev", "isort", cwd=PROJECT_DIRECTORY)
    execute("poetry", "add", "--lock", "--dev", "pytest-cov", cwd=PROJECT_DIRECTORY)
    execute("poetry", "add", "--lock", "--dev", "coverag", cwd=PROJECT_DIRECTORY)
    execute("poetry", "add", "--lock", "--dev", "bump2version", cwd=PROJECT_DIRECTORY)
    execute("poetry", "add", "--lock", "--dev", "pre-commit", cwd=PROJECT_DIRECTORY)
    execute("poetry", "add", "--lock", "--dev", "twine", cwd=PROJECT_DIRECTORY)
    execute("poetry", "add", "--lock", "--dev", "tox", cwd=PROJECT_DIRECTORY)

    execute("poetry", "add", "--lock", "--optional", "mkdocs", cwd=PROJECT_DIRECTORY)
    execute(
        "poetry",
        "add",
        "--dev",
        "--optional",
        "mkdocs-include-markdown-plugin",
        cwd=PROJECT_DIRECTORY,
    )
    execute("poetry", "add", "--lock", "--optional", "mkdocs-material", cwd=PROJECT_DIRECTORY)
    execute("poetry", "add", "--lock", "--optional", "mkdocstrings", cwd=PROJECT_DIRECTORY)
    execute(
        "poetry",
        "add",
        "--lock",
        "--dev",
        "--optional",
        "mkdocs-material-extensions",
        cwd=PROJECT_DIRECTORY,
    )
    execute("poetry", "add", "--lock", "--optional", "mkdocs-autoref", cwd=PROJECT_DIRECTORY)


def install_pre_commit_hooks():
    execute("poetry", "install", cwd=PROJECT_DIRECTORY)
    execute("poetry", "run", "pre_commit", "install", cwd=PROJECT_DIRECTORY)


if __name__ == "__main__":
    use_click = "{{ cookiecutter.command_line_interface|lower }}" == "click"
    use_mypy = "{{ cookiecutter.use_mypy }}" == "y"
    cicd = "{{ cookiecutter.cicd }}"
    add_deps = "{{ cookiecutter.newest_deps }}" == "y"

    if not use_click:
        cli_file = os.path.join("{{ cookiecutter.pkg_name }}", "cli.py")
        remove_file(cli_file)

    if not cicd == "all":
        preview_file = os.path.join(".github", "workflows", "preview.yml")
        release_file = os.path.join(".github", "workflows", "release.yml")
        remove_file(preview_file)
        remove_file(release_file)

    if not cicd == "dev":
        dev_file = os.path.join(".github", "workflows", "dev.yml")
        remove_file(dev_file)

    if "Not open source" == "{{ cookiecutter.open_source_license }}":
        remove_file("LICENSE")

    if add_deps:
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
