Linting your tests
==================

.. post::
   :author: Michal Bultrowicz
   :tags: Python, quality_assurance

Tests **are** a part of the codebase. So the should also meet some quality standards.
Here, we're gonna show how to lint them with Pylint or flake8.

Flake8 is less picky, so no different configuration is needed.

For pylint, the tests' linting configuration differs in disabled warnings: missing-docstring
(names should be descriptive enough, but maybe I'm wrong, who knows).
See what would happen if I'd run pylint on Pydas or Mountepy.

