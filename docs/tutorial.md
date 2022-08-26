# Tutorial

To start with, you will need [GitHub], [PyPI] and [TestPyPI] accounts. If
you don't have one, please follow the links to apply one before you get started on this
tutorial.

If you are new to Git and GitHub, you should probably spend a few minutes on
some tutorials at the top of the page at [GitHub Help].

## Step 1: Install Cookiecutter

Install [cookiecutter](https://cookiecutter.readthedocs.io/en/stable/installation.html)

## Step 2: Generate Your Package

Now it's time to generate your Python package.

Run the following command and feed with answers, If you don’t know what to enter, stick with the defaults:

```bash
cookiecutter https://github.com/mishamsk/cookiecutter-pypackage.git
```

A new folder will be created under current folder, the name is the answer you
provided to `project_slug`.

Go to this generated folder, the project layout should look like:

```
.
├── .bumpversion.cfg
├── .editorconfig
├── .github
│   ├── ISSUE_TEMPLATE.md
│   └── workflows
│       ├── dev.yml
│       ├── preview.yml
│       └── release.yml
├── .gitignore
├── .pre-commit-config.yaml
├── CHANGELOG.md
├── CONTRIBUTING.md
├── LICENSE
├── README.md
├── docs
│   ├── api.md
│   ├── changelog.md
│   ├── contributing.md
│   ├── index.md
│   ├── installation.md
│   └── usage.md
├── Makefile
├── mkdocs.yml
├── my_package
│   ├── __init__.py
│   ├── cli.py
│   └── my_package.py
├── pyproject.toml
├── setup.cfg
├── tox.ini
└── tests
    ├── __init__.py
    └── test_my_package.py

```

Here the project_slug is `my-package`, when you generate yours, it could be other name.

Also notice that the `pyproject.toml` in this folder. This is the main configuration file of our project.

## Step 3: Install Poetry

Install Poetry if you are not using it ([official docs](https://python-poetry.org/docs/master/#installing-with-pipx)). The whole project is managed by it.

## Step 4: Install Dev Requirements

You should still be in the folder named as `project_slug`, which containing the
 `pyproject.toml` file.

Install the new project's local development requirements with `poetry install`:

``` bash
poetry install
poetry run tox
```

Poetry will create its own virtualenv isolated from your system and install the dependencies in it.

We also launch a smoke test here by running `poetry run tox`. This will run `tox` within created virtual environment, give you a test report and lint report. You should see no errors except some lint warnings.

You can also activate the virtual environment manually with `poetry shell`, this will create a new shell.

## Step 5: Create a GitHub Repo

Go to your GitHub account and create a new repo named `my-package`, where
`my-package` matches the `project_slug` from your answers to running
cookiecutter.

Then go to repo > settings > secrets, click on 'New repository secret', add the following
 secrets:

- TEST_PYPI_API_TOKEN, see [How to apply TestPyPI token]
- PYPI_API_TOKEN, see [How to apply pypi token]

## Step 6: Upload code to GitHub

Back to your develop environment, find the folder named after the `project_slug`.
Move into this folder, and then setup git to use your GitHub repo and upload the
code:

``` bash
cd my-package

git add .
git commit -m "Initial commit."
git branch -M main
git remote add origin git@github.com:myusername/my-package.git
git push -u origin main
```

Where `myusername` and `my-package` are adjusted for your username and
repo name.

You'll need a ssh key to push the repo. You can [Generate] a key or
[Add] an existing one.

???+ Warning

    if you answered 'yes' to the question if install pre-commit hooks at last step,
    then you should find pre-commit be invoked when you run `git commit`, and some files
     may be modified by hooks. If so, please add these files and **commit again**.

### Check result

After pushing your code to GitHub, goto GitHub web page, navigate to your repo, then
click on actions link, you should find screen like this:

![](http://images.jieyu.ai/images/202104/20210419170304.png)

There should be some workflows running. After they finished, go to [TestPyPI], check if a
new artifact is published under the name `project_slug`.

## Step 7. Check documentation

Documentation will be published and available at *https://{your_github_account}.github.io/{your_repo}* once:

1. the commit is tagged, and the tag name is started with 'v' (lower case)
2. build/testing executed by GitHub CI passed

If you'd like to see what it's look like now, you could run the following command:

```
poetry run mkdocs serve
```

This will run the builtin development server for you to preview.

## Step 8. Make official release

  After done with your phased development in a feature branch, make a pull request, following
  instructions at [release checklist](pypi_release_checklist.md), trigger first official release and check
  result at [PyPI].


[Edit this file]: https://github.com/mishamsk/cookiecutter-pypackage/blob/master/docs/tutorial.md
[PYPI]: https://pypi.org
[GitHub]: https://github.com/
[TestPyPI]: https://test.pypi.org/
[GitHub Help]: https://help.github.com/
[Generate]: https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/
[Add]: https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account/
[How to apply testpypi token]: https://test.pypi.org/manage/account/
[How to apply pypi token]: https://pypi.org/manage/account/
[How to apply personal token]: https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token
