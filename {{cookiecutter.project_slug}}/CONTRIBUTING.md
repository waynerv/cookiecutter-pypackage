# Contributing

Contributions are welcome, and they are greatly appreciated! Every little bit
helps, and credit will always be given.

You can contribute in many ways:

## Types of Contributions

### Report Bugs

Report bugs at https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/issues.

If you are reporting a bug, please include:

* Your operating system name and version.
* Any details about your local setup that might be helpful in troubleshooting.
* Detailed steps to reproduce the bug.

### Fix Bugs

Look through the GitHub issues for bugs. Anything tagged with "bug" and "help
wanted" is open to whoever wants to implement it.

### Implement Features

Look through the GitHub issues for features. Anything tagged with "enhancement"
and "help wanted" is open to whoever wants to implement it.

### Write Documentation

{{ cookiecutter.project_name }} could always use more documentation, whether as part of the
official {{ cookiecutter.project_name }} docs, in docstrings, or even on the web in blog posts,
articles, and such.

### Submit Feedback

The best way to send feedback is to file an issue at https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/issues.

If you are proposing a feature:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.
* Remember that this is a volunteer-driven project, and that contributions
  are welcome :)

## Get Started!

Ready to contribute? Here's how to set up `{{ cookiecutter.project_slug }}` for local development.

1. Fork the `{{ cookiecutter.project_slug }}` repo on GitHub.
2. Clone your fork locally

    ```shell
    $ git clone git@github.com:your_name_here/{{ cookiecutter.project_slug }}.git
    ```

3. Ensure [poetry](https://python-poetry.org/docs/) is installed.
4. Install dependencies and start your virtualenv:

    ```shell
    $ poetry install -E test -E doc -E dev
    ```

5. Create a branch for local development:

    ```shell
    $ git checkout -b name-of-your-bugfix-or-feature
    ```

    Now you can make your changes locally.

6. When you're done making changes, check that your changes pass the
   tests, including testing other Python versions, with tox:

    ```shell
    $ poetry run tox
    ```

7. Commit your changes and push your branch to GitHub:

    ```shell
    $ git add .
    $ git commit -m "Your detailed description of your changes."
    $ git push origin name-of-your-bugfix-or-feature
    ```

8. Submit a pull request through the GitHub website.

## Pull Request Guidelines

Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include tests.
2. If the pull request adds functionality, the docs should be updated. Put
   your new functionality into a function with a docstring, and describe how to use the
   feature in the [usage.md](/docs/usage.md) file.
3. The pull request should work for Python 3.8 and 3.9. Check
   https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/actions
   and make sure that the tests pass for all supported Python versions.

## Tips

```shell
$ poetry run pytest tests/test_{{ cookiecutter.pkg_name }}.py
```

To run a subset of tests.

## Deploying

New versions are deployed via [GitHub Actions](https://docs.github.com/en/actions/learn-github-actions):

* A push to the master branch will trigger a release on [TestPyPI](https://test.pypi.org/project/{{ cookiecutter.project_slug }}/).
* Publishing a new release on GitHub will trigger a release on [PyPI](https://pypi.org/project/{{ cookiecutter.project_slug }}/).
When making a release please note the following:
  * notwells follows [semantic versioning](https://semver.org/).
  * To document new releases please enable [auto-generate release notes](https://docs.github.com/en/repositories/releasing-projects-on-github/automatically-generated-release-notes) when creating a release.
