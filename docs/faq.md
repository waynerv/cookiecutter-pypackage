???+ Question
    # Explain these GitHub workflows yaml files?
    - `dev.yml`: define dev workflow, run on every push and pull requests to master,
    basically run all the tests against multiple versions and platforms.
    - `preview.yml`: define stage & preview workflow, run on every push to master, publish dev build to TestPyPI.
    - `release.yml`: define release & publish workflow, run on every tag push, create GitHub release,
    publish docs to GitHub Pages and built package to PyPI.
