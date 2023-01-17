Structural pattern matching made me ditch yapf for black
========================================================

.. post::
   :author: Michal Bultrowicz
   :tags: Python, quality_assurance

I prefer Yapf to Black, because it allows for some configuration, and doesn't always spill out the same code,
so I can affect the shape of lines. That often gives me a more readable code.

yapf won't format lines if they don't break the rules, to you can make it look like you want to.

Sadly, it doesn't support `structural pattern matching ("match-case") <https://peps.python.org/pep-0636/>`_
from Python 3.10, which I fell in love with.

So I have

Because I like lines ending with commas, and yapf doesn't add any characters, I had another tool - add-trailing-comma.

My makefile has stuff like this:

Would be nice if the release happened and I could go back to yapf.

https://github.com/psf/black/issues/2242
https://github.com/google/yapf/pull/986 - waiting for yapf 0.33...


.. code-block:: bash

    SOURCES:=main_package tests

    format:
    	@echo Running isort...
    	@poetry run isort .
    	@echo Running add-trailing-comma...
    	@poetry run add-trailing-comma --exit-zero-even-if-changed $(shell find $(SOURCES) -name "*.py")
    	@echo Running yapf...
    	@poetry run yapf -ir $(SOURCES)

    static_checks:
    	@echo Checking import sorting...
    	@poetry run isort -c .
    	@echo Checking code formatting...
    	@poetry run yapf -dr $(SOURCES)
    	@echo Linting...
    	@poetry run pylint $(SOURCES)

Config in ``pyproject.toml``:


.. code-block:: bash

    [tool.yapf]
    based_on_style = "google"
    column_limit = 120
    dedent_closing_brackets = true
    coalesce_brackets = true
    # TODO maybe set this
    # split_all_comma_separated_values = true
