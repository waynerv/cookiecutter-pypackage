============
Contributing
============

Contributions are welcome, and they are greatly appreciated! Every little bit
helps, and credit will always be given.

You can contribute in many ways:

Types of Contributions
----------------------

Report Bugs
~~~~~~~~~~~

Report bugs at https://github.com/mishamsk/cookiecutter-pypackage/issues

If you are reporting a bug, please include:

* Your operating system name and version.
* Any details about your local setup that might be helpful in troubleshooting.
* Detailed steps to reproduce the bug.

Fix Bugs
~~~~~~~~

Look through the GitHub issues for bugs. Anything tagged with "bug"
and "help wanted" is open to whoever wants to implement a fix for it.

Implement Features
~~~~~~~~~~~~~~~~~~

Look through the GitHub issues for features. Anything tagged with "enhancement"
and "help wanted" is open to whoever wants to implement it.

Write Documentation
~~~~~~~~~~~~~~~~~~~

Cookiecutter PyPackage could always use more documentation, whether as part of
the official docs, in docstrings, or even on the web in blog posts, articles,
and such.

Submit Feedback
~~~~~~~~~~~~~~~

The best way to send feedback is to file an issue at
https://github.com/mishamsk/cookiecutter-pypackage/issues.

If you are proposing a new feature:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.
* Remember that this is a volunteer-driven project, and that contributions
  are welcome :)

Pull Request Guidelines
-----------------------

Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include tests.

2. If the pull request adds functionality, the docs should be updated. Put your
   new functionality into a function with a docstring, and add the feature to
   the list in README.rst.

3. The pull request should work for Python 3.10 and up.

Add a New Test
--------------

When fixing a bug or adding features, it's good practice to add a test to
demonstrate your fix or new feature behaves as expected. These tests should
focus on one tiny bit of functionality and prove changes are correct.

To write and run your new test, follow these steps:

1. Add the new test to `tests/test_bake_project.py`. Focus your test on the
   specific bug or a small part of the new feature.

::

2. If you have already made changes to the code, stash your changes and confirm
   all your changes were stashed:

   .. code-block:: bash

        $ git stash
        $ git stash list

::

3. Run your test and confirm that your test fails. If your test does not fail,
   rewrite the test until it fails on the original code:

   .. code-block:: bash

        $ pytest ./tests

::

4. (Optional) Run the tests with tox to ensure that the code changes work with
   different Python versions:

   .. code-block:: bash

        $ tox

::

5. Proceed work on your bug fix or new feature or restore your changes. To
   restore your stashed changes and confirm their restoration:

   .. code-block:: bash

        $ git stash pop
        $ git stash list

::

6. Rerun your test and confirm that your test passes. If it passes,
   congratulations!

.. cookiecutter: https://github.com/mishamsk/cookiecutter-pypackage
.. git: https://git-scm.com/book/en/v2/Getting-Started-Installing-Git

